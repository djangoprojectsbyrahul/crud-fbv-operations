from django.db import models

# Create your models here.
class StudentRegister(models.Model):
    name = models.CharField(max_length = 30)
    marks = models.IntegerField()
