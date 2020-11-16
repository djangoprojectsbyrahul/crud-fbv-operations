from django.conf.urls import url
from testapp import views

urlpatterns = [
    url(r'^$', views.temp_cookie_count),
    url(r'^permanent/', views.perm_cookie_view),
]
