from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testapp.forms import SignUpForm
from django.http import HttpResponseRedirect

# Create your views here.


def home_view(request):
    return render(request, 'testapp/home.html')


@login_required
def java_exam_view(request):
    return render(request, 'testapp/javaexam.html')


@login_required
def python_exam_view(request):
    return render(request, 'testapp/pythonexam.html')


@login_required
def aptitude_exam_view(request):
    return render(request, 'testapp/aptitudeexam.html')


def logout_view(request):
    return render(request, 'testapp/logout.html')


def sign_up_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # if form.is_valid():
        #     form.save()
        user = form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request, 'testapp/signup.html', {'form': form})
