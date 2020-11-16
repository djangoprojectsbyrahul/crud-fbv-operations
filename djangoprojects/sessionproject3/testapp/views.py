from django.shortcuts import render
from testapp.forms import AddItemForm

# Create your views here.


def add_items_view(request):
    form = AddItemForm()
    if request.method == 'POST':
        name = request.POST['name']
        quantity = request.POST['quantity']
        request.session[name] = quantity
        request.session.set_expiry(120)
        print(request.session.get_expiry_age())
        print(request.session.get_expiry_date())
    return render(request, 'testapp/additems.html', {'form': form})


def display_items_view(request):
    return render(request, 'testapp/displayitems.html')
