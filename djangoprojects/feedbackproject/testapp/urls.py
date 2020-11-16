from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^feedback', views.student_feedback),
]
