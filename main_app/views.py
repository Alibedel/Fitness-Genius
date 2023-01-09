from django.shortcuts import render

from .models import Workout

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Welcome to our Workout app!</h1>')


def workouts_index(request):
  workouts = Workout.objects.all()
  return render(request, 'workouts/index.html', { 'workouts': workouts })
