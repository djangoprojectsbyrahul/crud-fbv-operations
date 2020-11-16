from django.conf.urls import url
from testapp import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^punejobs', views.pune_jobs_info),
    url(r'^mumbaijobs', views.mumbai_jobs_info),
    url(r'^chennaijobs', views.chennai_jobs_info),
    url(r'^bengjobs', views.beng_jobs_info),
    url(r'^hydjobs', views.hyd_jobs_info),
]
