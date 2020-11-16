from django.conf.urls import url
from testapp import views

urlpatterns =  [
    url(r'^$', views.display_view),
    url(r'^displayall/', views.display_all_view),
    url(r'^displaygt/', views.display_gtelte_view),
    url(r'^displayfieldlookup/', views.display_i_or_exact_view),
    url(r'^displayorview/', views.using_or_view),
    url(r'^displayandview/', views.using_and_view),
    url(r'^displaynotview/', views.using_not_view),
    url(r'^displayinview/', views.using_in_view),
    url(r'^displayunionview/', views.using_union_operation_view),
    url(r'^aggregateview/', views.aggregate_view),
    url(r'^ascendingview/', views.ascending_order_view),
    url(r'^descendingview/', views.descending_order_view),
    url(r'^customrangeview/', views.custom_range_view),
    url(r'^customsortview/', views.custom_sort_column),
]
