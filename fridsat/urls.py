from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fridsat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('django.contrib.auth.urls')),
    url(r'^', include('front.urls', namespace="front")),
    url(r'^', include('registration.urls', namespace="registration")),
    url(r'^', include('reviews.urls', namespace="reviews")),
    url('', include('social.apps.django_app.urls', namespace='social')),
    (r'^comments/', include('django_comments.urls')),
)
