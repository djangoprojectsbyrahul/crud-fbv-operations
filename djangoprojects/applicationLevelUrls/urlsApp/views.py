from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pune_jobs(request):
    s="<h1>Pune Jobs Related Information!!!!</h1>"
    return HttpResponse(s)

def hyd_jobs(request):
    s="<h1>Hyderabad Jobs Related Information!!!!</h1>"
    return HttpResponse(s)

def chn_jobs(request):
    s="<h1>Chennai Jobs Related Information!!!!</h1>"
    return HttpResponse(s)

def beng_jobs(request):
    s="<h1>Bengaluru Jobs Related Information!!!!</h1>"
    return HttpResponse(s)
