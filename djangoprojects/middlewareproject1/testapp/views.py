from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def welcome_demo(request):
    print('This line printed by view function while processing of request')
    # print(10/0)
    return HttpResponse('<h1>Custom Middleware Demo</h1>')
