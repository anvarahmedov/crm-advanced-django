from django.db import models

class Lead(models.Model):
    first_name = models.CharField
    last_name = models.CharField
    age = models.IntegerField

    
