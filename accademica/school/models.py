from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Program(models.Model):
    school = models.ForeignKey(School, related_name='programs', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Course(models.Model):
    program = models.ForeignKey(Program, related_name='courses', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)

    def __str__(self):
        return self.name
