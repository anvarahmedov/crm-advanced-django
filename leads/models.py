from django.db import models
from django.contrib.auth import AbstractUser

class User(AbstractUser):
    pass

class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


