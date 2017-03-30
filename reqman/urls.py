from django.conf.urls import url

from . import views

app_name = 'reqman'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<request_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^analyst/$', views.analyst_list, name='analyst_list'),
    url(r'^analyst/(?P<analyst_id>[0-9]+)/$', views.analyst, name='analyst'),
    url(r'^datasource/$', views.db_list, name='db_list'),
    url(r'^datasource/(?P<db_id>[0-9]+)/$', views.db, name='db'),
    url(r'^stakeholder/$', views.stake_list, name='stake_list'),
    url(r'^stakeholder/(?P<stake_id>[0-9]+)/$', views.stake, name='stake'),
    url(r'^request/$', views.request_new, name='request'),
    url(r'^request/new/$', views.request_new, name='request_new'),
    url(r'^stakeholder/new/$', views.stake_new, name='stake_new')
]
