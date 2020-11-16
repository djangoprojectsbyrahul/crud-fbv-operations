from django.conf.urls import url
from urlsApp import views

urlpatterns = [
    url(r'^punejobs/', views.pune_jobs),
    url(r'^hydjobs/', views.hyd_jobs),
    url(r'^chennaijobs/', views.chn_jobs),
    url(r'^bengjobs/', views.beng_jobs),
]
