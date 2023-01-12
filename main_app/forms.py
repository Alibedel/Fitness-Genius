from django.forms import ModelForm
from .models import Routine, Diet

class RoutineForm(ModelForm):
  class Meta:
    model = Routine
    fields = ['name']

class DietForm(ModelForm):
  class Meta:
    model = Diet
    fields = ['diet']
