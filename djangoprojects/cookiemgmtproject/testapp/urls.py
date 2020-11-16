from django.conf.urls import url
from testapp import views

urlpatterns = [
    url(r'^$', views.name_view),
    url(r'^age/', views.age_view),
    url(r'^girlfriend/', views.girlfriend_view),
    url(r'^results/', views.result_view),
]
