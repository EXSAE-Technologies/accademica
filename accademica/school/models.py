from django.db import models
from django.contrib.auth.models import User

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

class Profile(models.Model):
    user=models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    gender=models.CharField(max_length=255,choices=[
        ('male','Male'),
        ('female','Female'),
        ('other','Other')
    ])
    date_of_birth=models.DateField()
    place_of_birth=models.CharField(max_length=255)
    nationality=models.CharField(max_length=255)
    marital_status=models.CharField(max_length=255,choices=[
        ('maried','Maried'),
        ('single','Single')
    ])
    national_id_or_passport=models.CharField(max_length=255)
    country=models.CharField(max_length=255)
    province=models.CharField(max_length=255)
    home_address=models.CharField(max_length=255)
    nok_full_name=models.CharField(max_length=255)
    nok_phone=models.CharField(max_length=255)
    nok_country=models.CharField(max_length=255)
    nok_province=models.CharField(max_length=255)
    nok_physical_adress=models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
