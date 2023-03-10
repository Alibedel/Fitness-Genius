from django.shortcuts import render, redirect

from .models import Workout, Photo
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RoutineForm, DietForm
import uuid
import boto3

# Add the following import
from django.http import HttpResponse

S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'workoutapp2023'

# Define the home view
@login_required
def home(request):
  return render(request, 'home.html')

@login_required
def workouts_index(request):
  workouts = Workout.objects.filter(user=request.user)
  return render(request, 'workouts/index.html', { 'workouts': workouts })

@login_required
def workouts_detail(request, workout_id):
  workout = Workout.objects.get(id=workout_id)
  routine_form = RoutineForm()
  diet_form = DietForm()
  return render(request, 'workouts/detail.html', {
    'workout': workout, 'routine_form': routine_form, 'diet_form': diet_form
    })

@login_required
def add_routine(request, workout_id):
  # create a ModelForm instance using the data in request.POST
  form = RoutineForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_routine = form.save(commit=False)
    new_routine.workout_id = workout_id
    new_routine.save()
  return redirect('detail', workout_id=workout_id)


@login_required
def add_diet(request, workout_id):
  # create a ModelForm instance using the data in request.POST
  form = DietForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_diet = form.save(commit=False)
    new_diet.workout_id = workout_id
    new_diet.save()
  return redirect('detail', workout_id=workout_id)

@login_required
def add_photo(request, workout_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url, workout_id=workout_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', workout_id=workout_id)





class WorkoutCreate(LoginRequiredMixin, CreateView):
  model = Workout
  fields = ['date', 'body']
  success_url = '/workouts/'
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)

    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)



class WorkoutUpdate(LoginRequiredMixin, UpdateView):
  model = Workout
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['date', 'body']
  success_url = '/workouts/'

class WorkoutDelete(LoginRequiredMixin, DeleteView):
  model = Workout
  success_url = '/workouts/'


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)





#secret access key :ZerjL+NsgxUpJS9dmoTsHS4VA3Uz7dNBBGEQDuqd
#access key id:AKIAR2PJNRVLEYYPIXVP
