from django.shortcuts import render

# Create your views here.
def hello(request):
    dir={'name':'Rahul'}
    return render(request,'testApp/hello.html',context=dir)
