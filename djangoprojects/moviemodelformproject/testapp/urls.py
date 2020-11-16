from django.conf.urls import url
from testapp import views

urlpatterns = [
    url(r'^$', views.index_view),
    url(r'^addmovie/', views.add_movie_view),
    url(r'^listmovie', views.list_movie_view),
]
