from django.shortcuts import render

# Create your views here.


def temp_cookie_count(request):
    count = int(request.COOKIES.get('count', 0))
    newcount = count + 1
    response = render(request, 'testapp/count.html', {'count': newcount})
    response.set_cookie('count', newcount)
    return response


def perm_cookie_view(request):
    count = int(request.COOKIES.get('count', 0))
    newcount = count + 1
    response = render(request, 'testapp/count.html', {'count': newcount})
    response.set_cookie('count', newcount, max_age=60)
    return response
