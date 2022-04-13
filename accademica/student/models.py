from django.db import models
from django.contrib.auth.models import User
from school.models import Program

# Create your models here.
class Student(models.Model):
    user=models.OneToOneField(User, related_name='student', on_delete=models.CASCADE)
    program=models.ForeignKey(Program, on_delete=models.CASCADE)
    year=models.IntegerField()

    def __str__(self):
        return self.user.username
    