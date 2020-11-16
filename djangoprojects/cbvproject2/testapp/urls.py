from django.conf.urls import url
from testapp import views

urlpatterns = [
    url(r'^$', views.BookListView.as_view()),
    url(r'^custombook/', views.BookCustomListView.as_view()),
    url(r'^defaultdetail/(?P<pk>\d+)/$', views.BookDetailView.as_view()),
]
