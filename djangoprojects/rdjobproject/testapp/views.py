from django.shortcuts import render
from testapp.models import *

# Create your views here.
def index(request):
    return render(request, "testapp/index.html")

def pune_jobs_info(request):
    pune_jobs = PuneJobs.objects.all()
    my_dict = {'pune_jobs':pune_jobs}
    return render(request, "testapp/punejobs.html", context = my_dict)

def mumbai_jobs_info(request):
    mumbai_jobs = MumbaiJobs.objects.all()
    my_dict = {'mumbai_jobs':mumbai_jobs}
    return render(request, "testapp/mumbaijobs.html", context = my_dict)

def beng_jobs_info(request):
    beng_jobs = BengJobs.objects.all()
    my_dict = {'beng_jobs':beng_jobs}
    return render(request, "testapp/bengjobs.html", context = my_dict)

def hyd_jobs_info(request):
    hyd_jobs = HydJobs.objects.all()
    my_dict = {'hyd_jobs':hyd_jobs}
    return render(request, "testapp/hydjobs.html", context = my_dict)

def chennai_jobs_info(request):
    chennai_jobs = ChennaiJobs.objects.all()
    my_dict = {'chennai_jobs':chennai_jobs}
    return render(request, "testapp/chennaijobs.html", context = my_dict)
