from django.conf.urls import url
from testapp import views

urlpatterns = [
    url(r'^$', views.BeerListView.as_view(), name='beers'),
    url(r'^detailview/(?P<pk>\d+)/$',
        views.BeerDetailView.as_view(), name='detail'),
    url(r'^createview/', views.BeerCreateView.as_view()),
    url(r'^updateview/(?P<pk>\d+)/$', views.BeerUpdateView.as_view()),
    url(r'^deleteview/(?P<pk>\d+)/$', views.BeerDeleteView.as_view()),
]
