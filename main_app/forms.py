from django.forms import ModelForm
from .models import Routine, Diet

class RoutineForm(ModelForm):
  class Meta:
    model = Routine
    fields = ['name', 'sets', 'reps']

class DietForm(ModelForm):
  class Meta:
    model = Diet
    fields = ['diet', 'grams']
