# Generated by Django 5.0.2 on 2024-03-03 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0003_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='status',
            field=models.BooleanField(default=False, verbose_name='статус подписки'),
        ),
    ]
