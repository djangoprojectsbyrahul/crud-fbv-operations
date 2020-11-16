from django.conf.urls import url
from testapp import views

urlpatterns = [
    url(r'^employee/', views.employee_view),
]
