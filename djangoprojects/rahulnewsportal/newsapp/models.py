from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30) #here max_length is madatory parameter
    marks=models.IntegerField()
