from rest_framework import serializers

from config import settings
from materials.models import Course, Lesson, Subscription
from materials.validators import VideoValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        validators = [VideoValidator(field='link_video')]
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField()
    is_subscribed = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)

    def get_count_lessons(self, instance):
        if instance.lesson_set.all().count():
            return instance.lesson_set.all().count()
        return 0

    def get_is_subscribed(self, course):
        """Проверяем, есть ли в наборе подписок курса объект
           с текущим пользователем"""
        request = self.context.get('request')
        if course.subscription_set.filter(user=request.user.id).exists():
            return True
        else:
            return False

    class Meta:
        model = Course
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
