from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mumbaiJob(request):
    msg="<h1>Hello Friend Greetings!!!!<br>At Mumbai in following companies Jobs are available</h1><hr>"
    msg=msg+"<h2>Post: Full stack web developer in PYTHON</h2>"
    msg=msg+"<ul><li>TCS</li>"
    msg=msg+"<li>Infosys</li>"
    msg=msg+"<li>Synechron</li>"
    msg=msg+"<li>Capgemini</li></ul>"
    return HttpResponse(msg)

def puneJob(request):
    msg="<h1>Hello Friend Greetings!!!!<br>At Pune in following companies Jobs are available</h1><hr>"
    msg=msg+"<h2>Post: Full stack web developer in PYTHON</h2>"
    msg=msg+"<ul><li>Calsoft</li>"
    msg=msg+"<li>Infosys</li>"
    msg=msg+"<li>Synechron</li>"
    msg=msg+"<li>Capgemini</li></ul>"
    return HttpResponse(msg)

def bengloreJob(request):
    msg="<h1>Hello Friend Greetings!!!!<br>At Bengalore in following companies Jobs are available</h1><hr>"
    msg=msg+"<h2>Post: Full stack web developer in PYTHON</h2>"
    msg=msg+"<ul><li>Calsoft</li>"
    msg=msg+"<li>Infosys</li>"
    msg=msg+"<li>TCS</li>"
    msg=msg+"<li>Capgemini</li></ul>"
    return HttpResponse(msg)

def hyderabadJob(request):
    msg="<h1>Hello Friend Greetings!!!!<br>At Hyderabad in following companies Jobs are available</h1><hr>"
    msg=msg+"<h2>Post: Selenium with PYTHON Automation Engineer</h2>"
    msg=msg+"<ul><li>TCS</li>"
    msg=msg+"<li>IBM</li>"
    msg=msg+"<li>TCS</li>"
    msg=msg+"<li>Capgemini</li></ul>"
    msg=msg+"<h3>*note: Here please meet DURGA sir he is very very good!!!!<br>Also enjoy Hyderabadi Biryani!!!!</h3>"
    return HttpResponse(msg)

def chennaiJob(request):
    msg="<h1>Hello Friend Greetings!!!!<br>At Chennai in following companies Jobs are available</h1><hr>"
    msg=msg+"<h2>Post: Selenium with JAVA Automation Engineer</h2>"
    msg=msg+"<ul><li>TCS</li>"
    msg=msg+"<li>IBM</li>"
    msg=msg+"<li>TCS</li>"
    msg=msg+"<li>Synechron</li></ul>"
    return HttpResponse(msg)
