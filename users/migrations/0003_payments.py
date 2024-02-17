# Generated by Django 5.0.2 on 2024-02-16 15:09

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
        ('users', '0002_alter_user_options_user_avatar_user_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_payments', models.DateField(default=django.utils.timezone.now, verbose_name='дата платежа')),
                ('paid_sum', models.FloatField(blank=True, null=True, verbose_name='сумма оплаты')),
                ('paid_method', models.CharField(blank=True, choices=[('наличными', 'cash'), ('перевод на счет', 'transfer')], null=True, verbose_name='метод оплаты')),
                ('paid_course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.course', verbose_name='оплаченный урок')),
                ('paid_lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.lesson', verbose_name='оплаченный урок')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
        ),
    ]
