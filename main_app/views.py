import uuid

import boto3
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import DietForm, RoutineForm
from .models import Workout

# S3 configuration is sourced from settings/environment - never hard-coded.
BUCKET = settings.AWS_STORAGE_BUCKET_NAME
S3_REGION = settings.AWS_S3_REGION
S3_BASE_URL = f"https://s3-{S3_REGION}.amazonaws.com/"


def landing(request):
    """Public landing page shown to anonymous visitors."""
    if request.user.is_authenticated:
        return redirect("index")
    return render(request, "landing.html")


@login_required
def home(request):
    return render(request, "home.html")


@login_required
def workouts_index(request):
    workouts = Workout.objects.filter(user=request.user).order_by("-date")
    return render(request, "workouts/index.html", {"workouts": workouts})


@login_required
def workouts_detail(request, workout_id):
    workout = Workout.objects.get(id=workout_id, user=request.user)
    routine_form = RoutineForm()
    diet_form = DietForm()
    return render(
        request,
        "workouts/detail.html",
        {"workout": workout, "routine_form": routine_form, "diet_form": diet_form},
    )


@login_required
def add_routine(request, workout_id):
    workout = Workout.objects.get(id=workout_id, user=request.user)
    form = RoutineForm(request.POST)
    if form.is_valid():
        new_routine = form.save(commit=False)
        new_routine.workout_id = workout.id
        new_routine.save()
    return redirect("detail", workout_id=workout_id)


@login_required
def add_diet(request, workout_id):
    workout = Workout.objects.get(id=workout_id, user=request.user)
    form = DietForm(request.POST)
    if form.is_valid():
        new_diet = form.save(commit=False)
        new_diet.workout_id = workout.id
        new_diet.save()
    return redirect("detail", workout_id=workout_id)


@login_required
def add_photo(request, workout_id):
    workout = Workout.objects.get(id=workout_id, user=request.user)
    photo_file = request.FILES.get("photo-file", None)
    if photo_file and BUCKET:
        s3 = boto3.client("s3")
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind("."):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            from .models import Photo

            Photo(url=url, workout_id=workout.id).save()
        except Exception as exc:  # narrow logging instead of a bare except
            print(f"Error uploading file to S3: {exc}")
    return redirect("detail", workout_id=workout_id)


class WorkoutCreate(LoginRequiredMixin, CreateView):
    model = Workout
    fields = ["date", "body"]
    success_url = "/workouts/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class WorkoutUpdate(LoginRequiredMixin, UpdateView):
    model = Workout
    fields = ["date", "body"]
    success_url = "/workouts/"

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)


class WorkoutDelete(LoginRequiredMixin, DeleteView):
    model = Workout
    success_url = "/workouts/"

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)


def signup(request):
    error_message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
        error_message = "Invalid sign up - try again"
    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "registration/signup.html", context)
