from django.urls import path

from materials.apps import MaterialsConfig
from rest_framework.routers import DefaultRouter

from materials.views import CourseViewSet, LessonCreateAPIView, LessonUpdateAPIView, LessonRetrieveAPIView, \
    LessonListAPIView, LessonDestroyAPIView, SubscribeAPIView

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'materials', CourseViewSet, basename='course')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-retrieve'),
    path('lessons/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'),

    path('course/<int:pk>/subscription/', SubscribeAPIView.as_view(), name='subscribe'),

] + router.urls
