from django.conf.urls import patterns, url
from django.conf import settings
from front import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^post/$', views.post, name='post'),
)
