from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
today = date.today()



class Workout(models.Model):

      date = models.DateField('Workout date', default= today)
      body = models.CharField(
        max_length=50
      )
      user = models.ForeignKey(User, on_delete=models.CASCADE)

    # def get_absolute_url(self):
    # return reverse('detail', kwargs={'workout_id': self.id})




class Routine(models.Model):
  name = models.CharField(max_length=50)
  sets = models.IntegerField()
  reps = models.IntegerField()

  workout = models.ForeignKey(Workout, on_delete=models.CASCADE)


class Diet(models.Model):
  diet = models.CharField(max_length=50)
  grams = models.IntegerField()

  workout = models.ForeignKey(Workout, on_delete=models.CASCADE)


class Photo(models.Model):
    url = models.CharField(max_length=200)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)

