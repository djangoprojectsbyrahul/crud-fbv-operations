from django.db import models
from django.db.models import Model

# Create your models here.


class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('eno')

    def get_emp_sal_range(self, esal1, esal2):
        return super().get_queryset().filter(esal__range=(esal1, esal2)).order_by('-esal')

    def get_sort_order(self, column_name):
        return super().get_queryset().order_by(column_name)


class CustomManager1(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('eno')


class CustomManager2(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(esal__gt=18000).order_by('esal')


class CustomManager3(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('ename')


class Employee(Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=128)
    esal = models.FloatField()
    ecity = models.CharField(max_length=128)
    #objects = CustomManager()
    objects = CustomManager1()


class ProxyEmployee1(Employee):
    objects = CustomManager2()

    class Meta:
        proxy = True


class ProxyEmployee2(Employee):
    objects = CustomManager3()

    class Meta:
        proxy = True
