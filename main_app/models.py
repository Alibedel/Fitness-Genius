from django.db import models
from datetime import date
today = date.today()




class Workout(models.Model):

      date = models.DateField('Workout date', default= today)
      body = models.CharField(
    max_length=50,
  )

    #   def __str__(self):
    #     return self.name
