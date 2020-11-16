from django.conf.urls import url
from testApp import views

urlpatterns = [
    url(r'^home/', views.home),
    url(r'^profile/', views.profile),    
]
