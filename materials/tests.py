from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from materials.models import Lesson, Course
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self) -> None:

        """Создание объектов для тестов"""
        self.client = APIClient()
        """Создание и авторизация тестового пользователя"""
        self.user = User.objects.create(id=1, email='test@test.test', password='12345')
        self.client.force_authenticate(user=self.user)
        """Создание тестовых курса и урока"""
        self.course = Course.objects.create(title='test_course', description='test_description')
        self.lesson = Lesson.objects.create(title='test_lesson', description='test_description',
                                            course=self.course, link_video='https://www.youtube.com/',
                                            owner=self.user)

    def test_create_lesson(self):
        """Тестирование создания урока"""
        data = {'title': 'test_lesson', 'description': 'test',
                'course': self.course.id, 'link_video': 'https://www.youtube.com/',
                'owner': self.user.id}
        response = self.client.post('/lesson/create/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Lesson.objects.filter(title=data['title']).exists())

    def test_retrieve_lesson(self):
        """Тестирование просмотра информации об уроке"""
        path = reverse('materials:lesson-retrieve', [self.lesson.id])
        response = self.client.get(path)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.lesson.title)

    def test_update_lesson(self):
        """Тестирование редактирования урока"""
        path = reverse('materials:lesson-update', [self.lesson.id])
        data = {'title': 'test-update', 'description': 'test'}
        response = self.client.patch(path, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.lesson.refresh_from_db()
        self.assertEqual(self.lesson.title, data['title'])

    def test_delete_lesson(self):
        """Тестирование удаления урока"""
        delete_url = reverse('materials:lesson-delete', args=[self.lesson.id])
        response = self.client.delete(delete_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Lesson.objects.filter(id=self.lesson.id).exists())


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()

        """Создание и авторизация тестового пользователя"""
        self.user = User.objects.create(id=1, email='test@test.test', password='12345')
        self.client.force_authenticate(user=self.user)

        """Создание тестового курса"""
        self.course = Course.objects.create(title='test_course', description='test')

        """Ссылка на контроллер управления подпиской"""
        self.path = reverse('materials:subscribe', [self.course.id])

    def test_sub_on(self):
        """Тестрование добавления подписки"""
        response = self.client.post(self.path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Подписка добавлена")

    def test_sub_off(self):
        """Тестрование удаления подписки (2 раза запущен процесс подписки)"""
        response = self.client.post(self.path)
        response = self.client.post(self.path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Подписка удалена")
