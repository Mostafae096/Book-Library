from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # fullname = models.CharField(max_length=100, blank=True)
    phoneNum = models.CharField(max_length=15, blank=True)
    bio = models.CharField(max_length=500, blank=True)
    joining_date = models.DateField(auto_now_add=True)
