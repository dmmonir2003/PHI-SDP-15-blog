from django.db import models

# Create your models here.


class Profiles(models.Model):
    name=models.CharField(max_length=100)
    about=models.TextField()
    