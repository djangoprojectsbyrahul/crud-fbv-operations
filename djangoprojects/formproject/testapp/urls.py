from django.conf.urls import url
from testapp import views

urlpatterns = [
    url(r'^register/', views.student_registration),
]
