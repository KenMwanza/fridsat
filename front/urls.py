from django.conf.urls import patterns, url
from django.conf import settings
from main import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
