from django.db import models

# Create your models here.
class applicants(models.Model):
    name = models.CharField(max_length=100)
    email =  models.CharField(max_length=50)
    pno=  models.IntegerField()
    clg =  models.CharField(max_length=100)
    branch =  models.CharField(max_length=100)
    year =   models.CharField(max_length=100)

