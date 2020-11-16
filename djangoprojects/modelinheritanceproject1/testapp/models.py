from django.db import models

# Create your models here.
# Below classes ContactInfo, Student, Teacher are examples for Abstract Base Class Model Inheritance


class ContactInfo(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    address = models.CharField(max_length=256)

    class Meta:
        abstract = True


class Student(ContactInfo):
    rollno = models.IntegerField()
    marks = models.IntegerField()


class Teacher(ContactInfo):
    subject = models.CharField(max_length=128)
    salary = models.FloatField()


# Below classes ContactInfo1, Student1 and Teacher1 are examples for Multitable Inheritance

class ContactInfo1(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    address = models.CharField(max_length=256)


class Student1(ContactInfo1):
    rollno = models.IntegerField()
    marks = models.IntegerField()


class Teacher1(ContactInfo1):
    subject = models.CharField(max_length=128)
    salary = models.FloatField()


# Below classes Parent, Child and SubChild are examples of Multilevel Inheritance

class Parent(models.Model):
    fd1 = models.CharField(max_length=128)
    fd2 = models.CharField(max_length=128)


class Child(Parent):
    fd3 = models.CharField(max_length=128)
    fd4 = models.CharField(max_length=128)


class SubChild(Child):
    fd5 = models.CharField(max_length=128)
