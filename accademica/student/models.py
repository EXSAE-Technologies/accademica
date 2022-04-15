from django.db import models
from django.contrib.auth.models import User
from school.models import Program, Course

# Create your models here.
class Student(models.Model):
    user=models.OneToOneField(User, related_name='student', on_delete=models.CASCADE)
    program=models.ForeignKey(Program, on_delete=models.CASCADE)
    year=models.IntegerField()

    def __str__(self):
        return self.user.username

class Grade(models.Model):
    student=models.ForeignKey(Student, related_name='grades', on_delete=models.CASCADE)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    total=models.FloatField(default=0.0)
    score=models.FloatField(default=0.0)
    grade=models.CharField(max_length=255,default='')
    comment=models.CharField(max_length=255,default='PROCEED')
    status=models.CharField(max_length=255, choices=[
        ('pending','PENDING'),
        ('approved','APPROVED'),
        ('declined','DECLINED')
    ])

    def __str__(self):
        return self.course.code