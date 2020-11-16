from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.post_display_view),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_display_view,
        name='post_list_by_tag_name'),
    # url(r'^$',views.PostListView.as_view()), #this is url for pagination using CBV
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.post_detail_view, name='post_detail'),
    url(r'^(?P<id>\d+)/share/$', views.mail_send_view),
    url(r'^(?P<id>\d+)/sharewhatsapp/$', views.whatsapp_send_view),
]
