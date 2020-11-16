from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wish_second(request):
    msg="<h1>Hello Guest Greeting from Second Application!!!!</h1>"
    return HttpResponse(msg)
