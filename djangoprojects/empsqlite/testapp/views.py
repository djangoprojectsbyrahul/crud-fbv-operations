from django.shortcuts import render
from testapp.models import Employee

# Create your views here.
def index(request):
    return render(request,'testapp/index.html')

def emp_info(request):
    emp_data=Employee.objects.all()
    my_dict={'emp_data':emp_data}
    return render(request,'testapp/emp.html',context=my_dict)
