# Generated by Django 4.1.4 on 2023-01-08 23:30

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
    ]
