from django.shortcuts import render
from testapp.models import *

# Create your views here.
def index(request):
    return render(request,'testapp/index.html')

def pune_jobs_info(request):
    pune_jobs = PuneJobs.objects.order_by('date')
    my_dict = {'pune_jobs':pune_jobs}
    return render(request,'testapp/punejobs.html',context=my_dict)
