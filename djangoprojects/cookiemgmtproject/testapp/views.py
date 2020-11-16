from django.shortcuts import render

# Create your views here.


def name_view(request):
    return render(request, 'testapp/name.html')


def age_view(request):
    name = request.GET['name']#Reading data from textfield with name='name' from name.html
    response = render(request, 'testapp/age.html')
    response.set_cookie('name', name)
    return response


def girlfriend_view(request):
    age = request.GET['age']
    response = render(request, 'testapp/girlfriend.html')
    response.set_cookie('age', age)
    return response


def result_view(request):
    gfname = request.GET['gfname']
    name = request.COOKIES.get('name')
    age = request.COOKIES.get('age')
    my_dict = {'gfname': gfname, 'name': name, 'age': age}
    return render(request, 'testapp/results.html', context=my_dict)
