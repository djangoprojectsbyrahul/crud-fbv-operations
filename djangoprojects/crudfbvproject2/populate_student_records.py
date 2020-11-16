import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','crudfbvproject2.settings')
import django
django.setup()

from faker import Faker
from testapp.models import Student
from random import *

faker=Faker()

def populate(n):
    for i in range(n):
        fsrollno=randint(100,999)
        fsname=faker.name()
        fsmarks=randint(40,100)
        fsaddr=faker.city()
        stud_record=Student.objects.get_or_create(srollno=fsrollno,sname=fsname,smarks=fsmarks,saddr=fsaddr)

populate(20)
