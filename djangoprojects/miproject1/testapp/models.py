from django.db import models

# Create your models here.

# Below classes ContactInfo, Student, Teacher are examples for Abstract Base Class Model Inheritance


class ContactInfo1(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    address = models.CharField(max_length=256)

    class Meta:
        abstract = True


class Student1(ContactInfo1):
    rollno = models.IntegerField()
    marks = models.IntegerField()


class Teacher1(ContactInfo1):
    subject = models.CharField(max_length=128)
    salary = models.FloatField()
