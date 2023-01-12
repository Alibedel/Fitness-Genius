from django.contrib import admin
# import your models here
from .models import Workout, Routine, Diet

# Register your models here
admin.site.register(Workout)

admin.site.register(Routine)

admin.site.register(Diet)
