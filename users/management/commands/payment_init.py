from django.core.management import BaseCommand

from materials.models import Course, Lesson
from users.models import Payments, User


class Command(BaseCommand):
    def handle(self, *args, **options):

        payment = Payments.objects.create(
            user=User.objects.get(pk=1),
            paid_course=Course.objects.get(pk=1),
            paid_sum=1000.00,
            paid_method="наличные"
        )

        payment.save()

        payment1 = Payments.objects.create(
            user=User.objects.get(pk=1),
            paid_lesson=Lesson.objects.get(pk=1),
            paid_sum=1000.00,
            paid_method="перевод на карту"
        )

        payment1.save()
