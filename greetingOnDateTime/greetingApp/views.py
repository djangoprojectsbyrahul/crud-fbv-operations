from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def greeting(request):
    date=datetime.datetime.now()
    current_hour=int(date.strftime("%H"))
    msg="<h1>Hello Guest "
    if current_hour<12:
        msg=msg+"Good Morning!!!!"
    elif current_hour<16:
        msg=msg+"Good Afternoon!!!!"
    elif current_hour<21:
        msg=msg+"Good Evening!!!!"
    else:
        msg=msg+"Good Night"
    msg=msg+"</h1><hr>"
    msg=msg+"<h1>Current Server time is : "+str(date)+"</h1>"
    return HttpResponse(msg)
