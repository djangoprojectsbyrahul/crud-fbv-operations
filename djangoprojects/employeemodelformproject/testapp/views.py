from django.shortcuts import render
from testapp import forms

# Create your views here.
def employee_view(request):
    form = forms.EmployeeRegister()
    if request.method=='POST':
        form = forms.EmployeeRegister(request.POST)
        if form.is_valid():
            form.save(commit = True)
            print("Inserted data into database successfully!!")
    return render(request, 'testapp/employee.html', {'form':form})            
