from django.conf.urls import url
from testapp import views

urlpatterns = [
    url(r'^inbuilt/', views.different_filter_view),
    url(r'^custom/', views.custom_filters_view),
]
