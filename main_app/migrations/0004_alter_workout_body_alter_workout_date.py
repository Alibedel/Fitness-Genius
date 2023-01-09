# Generated by Django 4.1.5 on 2023-01-09 00:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_workout_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='body',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='workout',
            name='date',
            field=models.DateField(default=datetime.date(2023, 1, 9), verbose_name='Workout date'),
        ),
    ]
