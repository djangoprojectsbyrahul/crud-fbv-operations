from django.shortcuts import render
from . import forms

# Create your views here.
def student_registration(request):
    form = forms.StudentRegistration()
    return render(request, 'testapp/register.html',{'form':form})
