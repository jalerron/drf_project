from django.core.management import BaseCommand
from django.core.management import call_command

from materials.models import Lesson, Course
from users.models import Payments


class Command(BaseCommand):

    def handle(self, *args, **options):
        Payments.objects.all().delete()
        Lesson.objects.all().delete()
        Course.objects.all().delete()

        call_command('loaddata', 'data.json')
