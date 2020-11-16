from django.shortcuts import render
from testapp.models import Book
from django.views.generic import ListView, DetailView

# Create your views here.


class BookListView(ListView):  # ListView with default template and context object
    model = Book
    # here default template is : book_list.html
    # default context object is : book_list


# ListView with our template and context object
class BookCustomListView(ListView):
    model = Book
    template_name = 'testapp/book.html'
    context_object_name = 'list_of_books'
    # now here template is : book.html
    # and context object is : list_of_books


class BookDetailView(DetailView):  # DetailView with default template and context object
    model = Book
    # here default template is : book_detail.html
    # default context object is : book or object
