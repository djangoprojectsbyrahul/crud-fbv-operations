from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wish_first(request):
    msg="<h1>Hello Guest Greeting from First Application!!!!</h1>"
    return HttpResponse(msg)
