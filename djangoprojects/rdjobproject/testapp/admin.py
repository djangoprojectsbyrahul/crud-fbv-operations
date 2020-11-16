from django.contrib import admin
from testapp.models import *

class PuneJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']

class MumbaiJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']

class HydJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']

class BengJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']

class ChennaiJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']

# Register your models here.
admin.site.register(PuneJobs,PuneJobsAdmin)
admin.site.register(MumbaiJobs,MumbaiJobsAdmin)
admin.site.register(HydJobs,HydJobsAdmin)
admin.site.register(BengJobs,BengJobsAdmin)
admin.site.register(ChennaiJobs,ChennaiJobsAdmin)
