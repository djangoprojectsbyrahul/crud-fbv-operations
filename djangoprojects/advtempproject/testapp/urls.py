from django.conf.urls import url
from testapp import views

urlpatterns = [
    url(r'^$', views.home_view),
    url(r'^sports/', views.sports_view),
    url(r'^movies/', views.movies_view),
    url(r'^politics/', views.politics_view),
]
