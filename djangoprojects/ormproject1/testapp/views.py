from django.shortcuts import render
from testapp.models import Employee
from django.db.models import Q
from django.db.models import Avg, Sum, Min, Max, Count


# Create your views here.


def display_view(request):
    return render(request, 'testapp/index.html')


def display_all_view(request):
    employee = Employee.objects.all()
    return render(request, 'testapp/display.html', {'employee': employee})


def display_gtelte_view(request):
    # we can use __gt, __gte, __lt, __lte etc
    employee = Employee.objects.filter(esal__gt=10000)
    return render(request, 'testapp/display.html', {'employee': employee})


def display_i_or_exact_view(request):
    # we can use __exact, __iexact, __contains, __icontains, __startswith, __istartswith, __endwith, __iendswith, __range

    # employee = Employee.objects.filter(id__exact = 2)
    # employee = Employee.objects.filter(ename__exact='Rahul Desai')
    # employee = Employee.objects.filter(ename__contains='ll')
    # employee = Employee.objects.filter(ename__istartswith='r')
    # employee = Employee.objects.filter(ename__iendswith='ll')
    employee = Employee.objects.filter(esal__range=(10000, 20000))
    return render(request, 'testapp/display.html', {'employee': employee})


def using_or_view(request):
    # way 1: Employee.objects.filter(esal__range=(10000, 20000))|Employee.objects.filter(ename__istartswith='R')
    # way 2: employee = Employee.objects.filter(Q(esal__range(18000, 20000)) | Q(ename__iendswith='i'))

    # employee = Employee.objects.filter(esal__range=(
    #     18000, 20000)) | Employee.objects.filter(ename__istartswith='R')

    employee = Employee.objects.filter(
        Q(esal__range=(18000, 20000)) | Q(ename__iendswith='i'))
    return render(request, 'testapp/display.html', {'employee': employee})


def using_and_view(request):
    # way 1: Employee.objects.filter(esal__range=(10000, 19000),ename__startswith='r')
    # way 2: Employee.objects.filter(Q(esal__range=(10000, 19000))&Q(ename__startswith='r'))
    # way 3: Employee.objects.filter(esal__range=(10000, 19000)) & Employee.objects.filter(ename__startswith='r')

    # employee = Employee.objects.filter(esal__range=(10000, 19000),ename__startswith='r')
    # employee = Employee.objects.filter(Q(esal__range=(10000, 19000))&Q(ename__startswith='r'))
    employee = Employee.objects.filter(esal__range=(
        10000, 19000)) & Employee.objects.filter(ename__startswith='r')
    return render(request, 'testapp/display.html', {'employee': employee})


def using_not_view(request):
    # way 1: Employee.object.exclude(esal__range=(16000,20000))
    # way 2: Employee.object.filter(~Q(ename__startwith='r'))

    # employee = Employee.objects.exclude(esal__range=(16000,20000))
    employee = Employee.objects.filter(~Q(esal__range=(12000, 20000)))
    return render(request, 'testapp/display.html', {'employee': employee})


def using_in_view(request):
    employee = Employee.objects.filter(id__in=[1, 2, 3, 4, 5, 6, 7, 8, ])
    return render(request, 'testapp/display.html', {'employee': employee})


def using_union_operation_view(request):
    qs1 = Employee.objects.filter(esal__range=(12000, 13000))
    qs2 = Employee.objects.filter(ename__istartswith='r')
    employee = qs2.union(qs1)
    return render(request, 'testapp/display.html', {'employee': employee})


def aggregate_view(request):
    avg = Employee.objects.all().aggregate(Avg('esal'))
    sum = Employee.objects.all().aggregate(Sum('esal'))
    min = Employee.objects.all().aggregate(Min('esal'))
    max = Employee.objects.all().aggregate(Max('esal'))
    count = Employee.objects.all().aggregate(Count('esal'))
    my_dict = {'avg': avg, 'sum': sum, 'min': min, 'max': max, 'count': count}
    return render(request, 'testapp/aggregate.html', context=my_dict)


def ascending_order_view(request):
    # employee = Employee.objects.all().order_by('esal') #this will display all records
    employee = Employee.objects.all().order_by(
        'esal')[0:3]  # this will display top 3 records
    return render(request, 'testapp/display.html', {'employee': employee})


def descending_order_view(request):
    # employee = Employee.objects.all().order_by('esal') #this will display all records
    employee = Employee.objects.all().order_by(
        '-esal')[0:3]  # this will display top 3 records
    return render(request, 'testapp/display.html', {'employee': employee})


def custom_range_view(request):
    employee = Employee.objects.get_emp_sal_range(12000, 14000)
    return render(request, 'testapp/display.html', {'employee': employee})


def custom_sort_column(request):
    employee = Employee.objects.get_sort_order('-ename')
    return render(request, 'testapp/display.html', {'employee': employee})
