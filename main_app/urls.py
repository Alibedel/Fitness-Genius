from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('workouts/', views.workouts_index, name='index'),
  path('workouts/<int:workout_id>/', views.workouts_detail, name='detail'),
  path('workouts/create/', views.WorkoutCreate.as_view(), name='workouts_create'),
  path('workouts/<int:pk>/update/', views.WorkoutUpdate.as_view(), name='workouts_update'),
  path('workouts/<int:pk>/delete/', views.WorkoutDelete.as_view(), name='workouts_delete'),
  path('workouts/<int:workout_id>/add_routine/', views.add_routine, name='add_routine'),
  path('workouts/<int:workout_id>/add_diet/', views.add_diet, name='add_diet'),
  path('workouts/<int:workout_id>/add_photo/', views.add_photo, name='add_photo'),
  path('accounts/signup/', views.signup, name='signup'),

]
