from django.db import models
from django.urls import reverse
from datetime import date
today = date.today()



class Workout(models.Model):

      date = models.DateField('Workout date', default= today)
      body = models.CharField(
        max_length=50
      )
    

    # def get_absolute_url(self):
    # return reverse('detail', kwargs={'workout_id': self.id})


#gooooooooood work