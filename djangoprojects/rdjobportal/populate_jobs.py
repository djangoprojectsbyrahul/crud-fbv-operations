import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','rdjobportal.settings')
import django
django.setup()

from faker import Faker
from testapp.models import *
from random import *

faker = Faker()

def generate_phone_number():
    first_digit = randint(7,9)
    num = ''+str(first_digit)
    for i in range(9):
        num = num + str(randint(0,9))
    return int(num)

def populate(total_records, model_class):
    for i in range(total_records):
        fdate = faker.date()        
        fcompany = faker.company()
        ftitle = faker.random_element(elements = ('Project Manager', 'Business Analyst', 'Team Lead', 'Software Engineer'))
        feligibility = faker.random_element(elements = ('B.Tech','M.Tech','PhD','MCA'))
        faddress = faker.address()
        femail = faker.email()
        fphonenumber = generate_phone_number()
        pune_jobs_records = model_class.objects.get_or_create(date = fdate, company = fcompany, title = ftitle, eligibility = feligibility, address = faddress, email = femail, phonenumber = fphonenumber)

populate(50,PuneJobs)
