from django.conf.urls import url

from . import views

app_name = 'reqman'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<request_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^analyst/$', views.analyst_list, name='analyst_list'),
    url(r'^analyst/(?P<analyst_id>[0-9]+)/$', views.analyst, name='analyst'),
    url(r'^datasource/$', views.db_list, name='db_list'),
    url(r'^datasource/(?P<db_id>[0-9]+)/$', views.db, name='db')
]
