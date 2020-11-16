from django.db import models

# Create your models here.
class Sample(models.Model):
    sr_no=models.IntegerField()
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
