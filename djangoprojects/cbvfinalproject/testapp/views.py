from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from testapp.models import Beer
from django.core.urlresolvers import reverse_lazy

# Create your views here.


class BeerListView(ListView):
    model = Beer


class BeerDetailView(DetailView):
    model = Beer


class BeerCreateView(CreateView):
    model = Beer
    # or we can write fields=('brand','taste','color','price')
    fields = '__all__'


class BeerUpdateView(UpdateView):
    model = Beer
    fields = ('taste', 'color', 'price')


class BeerDeleteView(DeleteView):
    model = Beer
    success_url = reverse_lazy('beers')
