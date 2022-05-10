from django.contrib import admin
from .models import School, Program, Course
from .models import Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(School)
admin.site.register(Program)
admin.site.register(Course)