from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    stmt1='<h1 style="color:blue;background:black;">Hello Welcome to DJango Classes....DJango is Nursery Level Concept.</h1>'
    stmt2='<h2 style="color:blue;background:black;">This is Rahul Desai from Manas Lake.</h2>'
    stmt3='<h2 style="color:blue;background:black;">Below are my favourite Drinks:</h2>'
    stmt4='<ol style="color:red;font-size:20px;"><li>Mc Dowells No. 1</li>'
    stmt5='<li>Signature</li>'
    stmt6='<li>Blenders pride</li>'
    stmt7='<li>Teachers</li></ol>'
    msg=stmt1+stmt2+stmt3+stmt4+stmt5+stmt6+stmt7
    return HttpResponse(msg)
