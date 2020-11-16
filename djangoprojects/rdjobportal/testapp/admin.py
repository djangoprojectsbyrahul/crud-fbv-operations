from django.contrib import admin
from testapp.models import *

class PuneJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']

# Register your models here.
admin.site.register(PuneJobs,PuneJobsAdmin)
