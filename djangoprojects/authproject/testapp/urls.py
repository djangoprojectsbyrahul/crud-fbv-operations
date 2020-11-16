from django.conf.urls import url
from testapp import views

urlpatterns = [
    url(r'^$', views.home_view),
    url(r'^javaexam/', views.java_exam_view),
    url(r'^pythonexam/', views.python_exam_view),
    url(r'^aptitudeexam/', views.aptitude_exam_view),
    url(r'^logout/', views.logout_view),
    url(r'^signup/', views.sign_up_view),
]
