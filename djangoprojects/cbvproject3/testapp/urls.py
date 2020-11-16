from django.conf.urls import url
from testapp import views

urlpatterns = [
    url(r'^$', views.CompanyListView.as_view(), name='companies'),
    url(r'^companydetail/(?P<pk>\d+)/$',
        views.CompanyDetailView.as_view(), name='detail'),  # need to specify name so we can use it inside models.py company class's get_absolute_url method
    url(r'^companycreate/', views.CompanyCreateView.as_view()),
    url(r'^companyupdate/(?P<pk>\d+)/$', views.CompanyUpdateView.as_view()),
    url(r'^companydelete/(?P<pk>\d+)/$', views.CompanyDeleteView.as_view()),
]
