from django.conf.urls import patterns, url
from django.conf import settings
from front import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^publish/$', views.publish, name='publish'),
)
