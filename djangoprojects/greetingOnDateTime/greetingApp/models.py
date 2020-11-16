from django.db import models

# Create your models here.
class Student_Second(models.Model):
    roll_no=models.IntegerField()
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    marks=models.IntegerField()
