from django.conf.urls import url
from testApp import views

urlpatterns = [
    url(r'^datetime/', views.date_info)
]
