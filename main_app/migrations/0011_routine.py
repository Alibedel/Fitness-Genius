# Generated by Django 4.1.4 on 2023-01-12 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_alter_workout_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.workout')),
            ],
        ),
    ]
