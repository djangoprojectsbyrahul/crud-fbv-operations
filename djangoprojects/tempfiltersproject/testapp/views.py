from django.shortcuts import render
from testapp.models import FilterDemo

# Create your views here.


def different_filter_view(request):
    filter_list = FilterDemo.objects.all()
    return render(request, 'testapp/tempfilters.html', {'filter_list': filter_list})


def custom_filters_view(request):
    filter_list = FilterDemo.objects.all()
    return render(request, 'testapp/custtemplate.html', {'filter_list': filter_list})
