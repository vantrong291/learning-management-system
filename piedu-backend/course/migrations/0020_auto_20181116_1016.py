# Generated by Django 2.1 on 2018-11-16 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0019_auto_20181116_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='day_of_week',
            field=models.CharField(max_length=5, verbose_name='Day Of Week'),
        ),
    ]
