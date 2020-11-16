from django.shortcuts import render, redirect
from testapp.models import Student
from testapp.forms import StudentForm

# Create your views here.


def retrieve_view(request):
    students = Student.objects.all()
    return render(request, 'testapp/index.html', {'students': students})


def create_view(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return redirect('/testapp')
    return render(request, 'testapp/create.html', {'form': form})


def delete_view(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/testapp')


def update_view(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/testapp')
    return render(request, 'testapp/update.html', {'student': student})
