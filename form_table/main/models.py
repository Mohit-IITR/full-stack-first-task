from operator import mod
from django.db import models

# Create your models here.
class Applicants(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=60)
    pnumber = models.IntegerField()
    college = models.CharField(max_length=200)
    branch = models.CharField(max_length=50)
    year = models.CharField(max_length=4)