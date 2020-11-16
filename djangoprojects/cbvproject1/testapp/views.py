from django.shortcuts import render
from django.views.generic import View
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.


class HelloWorld(View):
    def get(self, request):
        return HttpResponse('<H1>This is from Class Based View</h1>')


class HelloWorldTemplateView(TemplateView):
    template_name = 'testapp/results.html'


class HellowWorldTemplateContext(TemplateView):
    template_name = 'testapp/info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "Hridhan"
        context['subject'] = "Operating System"
        context['marks'] = 100
        return context
