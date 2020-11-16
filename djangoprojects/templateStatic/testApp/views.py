from django.shortcuts import render

# Create your views here.
def home(request):
    my_dir = {'guest':'Rahul'}
    return render(request,'testApp/home.html', context=my_dir)

def profile(request):
    return render(request,'testApp/profile.html')
