# Generated by Django 5.0.2 on 2024-02-16 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_payments'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payments',
            options={'verbose_name': 'платеж', 'verbose_name_plural': 'платежи'},
        ),
    ]
