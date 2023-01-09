from django.db import models
from datetime import date
today = date.today()

BODY = (
    ('B', 'Back and Chest'),
    ('L', 'Legs'),
    ('A', 'Arms')
)


class Workout(models.Model):

      date = models.DateField('Workout date', default= today)
      body = models.CharField(
    max_length=1,
    choices=BODY,
    default=BODY[0][0]
  )

