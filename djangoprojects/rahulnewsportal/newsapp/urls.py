from django.conf.urls import url
from newsapp import views

urlpatterns=[
    url(r'^$', views.home),
    url(r'^sportsinfo/', views.sports_info),
    url(r'^moviesinfo/', views.movies_info),
    url(r'^politicsinfo/', views.politics_info),
]
