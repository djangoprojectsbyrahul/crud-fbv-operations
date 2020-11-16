import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','rdjobproject.settings')
import django
django.setup()

from testapp.models import *
from faker import Faker
from random import *
fake = Faker()
def phonenumbergen():
    digit_first = randint(7,9)
    num = '' + str(digit_first)
    for i in range(9):
        num = num + str(randint(0,9))
    return int(num)

def populate(n, city_class):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements = ('Project Manager', 'Team Lead', 'Software Engineer'))
        feligibility = fake.random_element(elements = ('B.E.', 'M.E.', 'MCA', 'PhD'))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = phonenumbergen()
        punejobs_record = city_class.objects.get_or_create(date = fdate, company = fcompany, title = ftitle, eligibility = feligibility, address = faddress, email = femail, phonenumber = fphonenumber)
populate(25,PuneJobs)
populate(25,MumbaiJobs)
populate(25,ChennaiJobs)
populate(25,BengJobs)
populate(25,HydJobs)
