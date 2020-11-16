import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crudfbvproject.settings')
import django
django.setup()


from random import *
from faker import Faker
from testapp.models import *
faker = Faker()


def populate(n):
    for i in range(n):
        feno = randint(1000, 9999)
        fename = faker.name()
        fesal = randint(10000, 20000)
        feaddr = faker.city()
        emp_record = Employee.objects.get_or_create(
            eno=feno, ename=fename, esal=fesal, eaddr=feaddr)


populate(20)
