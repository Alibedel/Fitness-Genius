# Generated by Django 4.1.5 on 2023-01-08 22:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_remove_workout_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='date',
            field=models.DateField(default=datetime.date(2023, 1, 8), verbose_name='Workout date'),
        ),
    ]