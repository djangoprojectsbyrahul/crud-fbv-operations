from django.conf.urls import url
from testapp import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^empinfo', views.emp_info),
]
