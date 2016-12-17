from django.conf.urls import url

from . import views

app_name = 'polls'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<Artist_id>[^/])/$', views.detail, name='detail'),
    url(r'^albumas/(?P<Album_id>[0-9]+)/$', views.albumas, name='albumas'),
    url(r'^member/(?P<Members_id>[0-9]+)/$', views.members, name='members'),
    url(r'^Single/(?P<Singles_id>[0-9]+)/$', views.single, name='single'),
]