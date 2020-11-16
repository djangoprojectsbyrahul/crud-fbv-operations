from django.conf.urls import url
from testapp import views

urlpatterns = [
    url(r'^$', views.welcome_demo),
]
