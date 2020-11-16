from django.conf.urls import url
from testapp import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^punejobs', views.pune_jobs_info),
]
