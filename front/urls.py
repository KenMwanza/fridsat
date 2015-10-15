from django.conf.urls import patterns, include, url
from front import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^home$', views.index, name='home'),
    url(r'^add-business/$', views.add_business, name='add_business'),
    url(r'^category/(?P<slug>[\w-]+)/$', views.category, name='category'),
    url(r'^(?P<slug>[\w-]+)/$', views.business, name='business'),
    url(r'^county/(?P<slug>[\w-]+)/$', views.county, name='county'),
    url(r'^(?P<county>[\w-]+)/(?P<area>[\w-]+)/$', views.area, name='area'),
    (r'^business/search', include('haystack.urls')),
)