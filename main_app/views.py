from django.shortcuts import render

from .models import Workout
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Welcome to our Workout app!</h1>')


def workouts_index(request):
  workouts = Workout.objects.all()
  return render(request, 'workouts/index.html', { 'workouts': workouts })

def workouts_detail(request, workout_id):
  workout = Workout.objects.get(id=workout_id)
  return render(request, 'workouts/detail.html', { 'workout': workout })




class WorkoutCreate(CreateView):
  model = Workout
  fields = '__all__'
  success_url = '/workouts/'



class WorkoutUpdate(UpdateView):
  model = Workout
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['date', 'body']
  success_url = '/workouts/'

class WorkoutDelete(DeleteView):
  model = Workout
  success_url = '/workouts/'
