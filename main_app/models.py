from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Workout(models.Model):
    date = models.DateField("Workout date", default=timezone.localdate)
    body = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.body} ({self.date})"

    def get_absolute_url(self):
        return reverse("detail", kwargs={"workout_id": self.id})


class Routine(models.Model):
    name = models.CharField(max_length=50)
    sets = models.IntegerField()
    reps = models.IntegerField()
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Diet(models.Model):
    diet = models.CharField(max_length=50)
    grams = models.IntegerField()
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)

    def __str__(self):
        return self.diet


class Photo(models.Model):
    url = models.CharField(max_length=200)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
