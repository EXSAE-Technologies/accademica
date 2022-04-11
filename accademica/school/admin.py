from django.contrib import admin
from .models import School, Program, Course

# Register your models here.
admin.site.register(School)
admin.site.register(Program)
admin.site.register(Course)