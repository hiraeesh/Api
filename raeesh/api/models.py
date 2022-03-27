from email.policy import default
from operator import mod
from unicodedata import name
from django.db import models

# Create your models here.
class Student(models.Model):
    id=models.IntegerField(primary_key=True,max_length=20)
    name=models.CharField(max_length=30)
    age=models.IntegerField(max_length=20)
    city=models.CharField(max_length=20)
    myimage=models.ImageField(default=0,upload_to='images/')
