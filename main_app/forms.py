from django.forms import ModelForm
from .models import Routine

class RoutineForm(ModelForm):
  class Meta:
    model = Routine
    fields = ['name']
