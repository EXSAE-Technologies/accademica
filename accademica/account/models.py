from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    debit=models.FloatField(default=0.0)
    credit=models.FloatField(default=0.0)
    ref=models.CharField(max_length=255)
    status=models.CharField(max_length=255,choices=[
        ('pending','PENDING'),
        ('approved','APPROVED'),
        ('declined','DECLINED')
    ])