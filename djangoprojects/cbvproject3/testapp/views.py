from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from testapp.models import Company
from django.core.urlresolvers import reverse_lazy

# Create your views here.


class CompanyListView(ListView):
    model = Company
    # here default template is: company_list.html and
    # default context object is: company_list


class CompanyDetailView(DetailView):
    model = Company
    # here default template is: company_detail.html
    # default context object is: company or object


class CompanyCreateView(CreateView):
    model = Company
    fields = ['name', 'location', 'ceo']  # these fields will appear on form
    # here default template is company_form.html


class CompanyUpdateView(UpdateView):
    model = Company
    fields = ['name', 'ceo']
    # this will use create view template for update and shows only name and ceo fields


class CompanyDeleteView(DeleteView):
    model = Company
    # this companies is value of name variable specified in urlpattern for ListView
    success_url = reverse_lazy('companies')
