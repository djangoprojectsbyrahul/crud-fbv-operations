import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ormproject1.settings')
import django
django.setup()

from faker import Faker
from random import *
from testapp.models import *

faker=Faker()
def populate(n):
    for i in range(n):
        feno=randint(1000,9999)
        fename=faker.name()
        fesal=randint(10000,20001)
        fecity=faker.city()
        employee_record=Employee.objects.get_or_create(eno=feno,ename=fename,esal=fesal,ecity=fecity)

populate(50)
