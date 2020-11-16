from django.conf.urls import url
from testApp import views

urlpatterns=[
    url(r'^hello',views.hello)
]
