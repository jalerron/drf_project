from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from materials.models import Course, Lesson, Subscription
from materials.pagination import MaterialsPagination
from materials.permissions import IsModerator, IsOwner
from materials.serializers import CourseSerializer, LessonSerializer, SubscriptionSerializer


class CourseViewSet(viewsets.ModelViewSet):
    pagination_class = MaterialsPagination
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        """Закрыл доступ к действиям пермишинами"""
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated, ~IsModerator]
        elif self.action in ['list', 'retrieve', 'update']:
            self.permission_classes = [IsModerator | IsOwner]
        elif self.action == 'destroy':
            self.permission_classes = [IsOwner]
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        """привязка создаваемого объекта к пользователю"""
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    def get_queryset(self):
        """закрыл объекты по пирммишену"""
        if not self.request.user.groups.filter(name='Модератор').exists():
            return Course.objects.filter(owner=self.request.user.id)
        return Course.objects.all()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        """привязка создаваемого объекта к пользователю"""
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator | IsOwner]


class LessonListAPIView(generics.ListAPIView):
    pagination_class = MaterialsPagination
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator | IsOwner]

    def get_queryset(self):
        """закрыл объекты по пирммишену"""
        if not self.request.user.groups.filter(name='Модератор').exists():
            return Lesson.objects.filter(owner=self.request.user.id)
        else:
            return Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator | IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner]


class SubscribeAPIView(APIView):
    """Контроллер управления подпиской пользователя на курс
       в запросе передаем id курса и если подписка на данный курс у текущего пользователя
       существует - удаляем, если нет - создаем"""
    serializer_class = SubscriptionSerializer

    @staticmethod
    def post(request, pk):
        queryset = Course.objects.filter(pk=pk)
        user = request.user
        course = get_object_or_404(queryset=queryset)
        subs_item = Subscription.objects.filter(course=course, user=user)

        if subs_item.exists():
            subs_item.delete()
            message = 'Подписка удалена'
        else:
            Subscription.objects.create(user=user, course=course)
            message = 'Подписка добавлена'
        return Response({"message": message})
