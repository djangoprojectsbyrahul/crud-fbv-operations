from django.conf.urls import url
from testapp import views

urlpatterns = [
    url(r'^classview', views.HelloWorld.as_view()),
    url(r'^templateclassview/', views.HelloWorldTemplateView.as_view()),
    url(r'^templateclasscontextview', views.HellowWorldTemplateContext.as_view()),
]
