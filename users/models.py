import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from materials.models import Lesson, Course

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):

    email = models.EmailField(unique=True, verbose_name='почта')
    full_name = models.CharField(max_length=150, verbose_name='полное имя', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    city = models.CharField(max_length=150, verbose_name='город', **NULLABLE)
    phone = models.CharField(max_length=15, verbose_name='телефон', **NULLABLE)

    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Payments(models.Model):

    CASH = 'наличныe'
    TRANSFER = 'перевод на счет'

    PAYMENT_METHOD_CHOISE = [
        (CASH, "Наличные"),
        (TRANSFER, "Перевод")
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    date_payments = models.DateField(auto_now_add=True, verbose_name='дата платежа')
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='оплаченный урок', **NULLABLE)
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='оплаченный урок', **NULLABLE)
    paid_sum = models.IntegerField(verbose_name='сумма оплаты', **NULLABLE)
    paid_method = models.CharField(choices=PAYMENT_METHOD_CHOISE, verbose_name='метод оплаты', **NULLABLE)

    payment_link = models.URLField(max_length=400, **NULLABLE, verbose_name='ссылка на оплату')
    payment_id = models.CharField(max_length=100, **NULLABLE, verbose_name='идентификатор платежа')

    def __str__(self):
        return f'{self.user} - {self.date_payments} - {self.paid_lesson if self.paid_lesson else self.paid_course} - {self.paid_method}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
        ordering = ('-date_payments',)
