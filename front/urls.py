from django.conf.urls import patterns, include, url
from front import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^home$', views.index, name='home'),
    url(r'^add-business/$', views.add_business, name='add_business'),
    url(r'^category/(?P<slug>[\w-]+)/$', views.category, name='category'),
    url(r'^(?P<slug>[\w-]+)/$', views.business, name='business'),
    url(r'^county/(?P<slug>[\w-]+)/$', views.county, name='county'),
    url(r'^county/(?P<county>[\w-]+)/(?P<area>[\w-]+)/$', views.area, name='area'),
    url(r'^custom/business-groups/$', views.custom_business_groups, name='custom_business_groups'),
    url(r'^custom-business-groups/(?P<slug>[\w-]+)/$', views.custom_business_group, name='custom_business_group'),
    (r'^business/search', include('haystack.urls')),
)