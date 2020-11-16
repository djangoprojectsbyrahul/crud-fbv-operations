from django.conf.urls import url
from testapp import views

urlpatterns = [
    url(r'^$', views.add_items_view),
    url(r'^display/', views.display_items_view),
]
