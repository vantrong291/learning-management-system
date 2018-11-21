# Generated by Django 2.1 on 2018-11-20 10:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0033_auto_20181118_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='students',
            field=models.ManyToManyField(through='course.ClassStudent', to=settings.AUTH_USER_MODEL),
        ),
    ]
