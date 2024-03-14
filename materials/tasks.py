from datetime import timedelta

from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from config.settings import EMAIL_HOST_USER
from materials.models import Subscription, Course
from users.models import User


@shared_task
def notifications_update_course(course_id):
    """ Отправка письма при обновлении курса """
    instance = Subscription.objects.filter(course=course_id)
    course = Course.objects.get(id=course_id)
    prev_data = course.update

    for elem in instance:
        # if prev_data < timezone.now():
        send_mail(
            subject=f'Обновление курса {course.title}!',
            message=f'Произошло обновление курса {course.title}, '
                    f'Вы можете просмотреть данные изменения в разделе данного курса.',
            from_email=EMAIL_HOST_USER,
            recipient_list=(elem.user.email,)
        )

    print('Выполнено')


@shared_task
def check_last_login():
    """ Проверка на активность профиля """

    users = User.objects.filter(is_active=True, is_superuser=False, last_login__isnull=False)

    for user in users:
        if user.last_login < (timezone.now() - timedelta(days=31)):
            user.is_active = False
            user.save()

    print('Проверка статуса пройдена')
