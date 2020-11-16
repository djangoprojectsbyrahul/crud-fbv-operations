from django.conf.urls import url
from testapp import views

urlpatterns = [
    url(r'^$', views.retrieve_view),
    url(r'^create/', views.create_view),
    url(r'^delete/(?P<id>\d+)/$', views.delete_view),
    url(r'^update/(?P<id>\d+)/$', views.update_view),
]
