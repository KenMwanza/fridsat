from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import FlatPageSitemap
from django.conf import settings
from django.contrib import admin
from front.sitemaps import BusinessSitemap, CountySitemap, CategorySitemap

sitemaps = {
    'flatpages': FlatPageSitemap,
    'business': BusinessSitemap,
    'county': CountySitemap,
    'category': CategorySitemap,
}

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fridsat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('django.contrib.auth.urls')),
    url(r'^', include('front.urls', namespace="front")),
    url(r'^reviews/', include('reviews.urls', namespace="reviews")),
    url(r'^', include('registration.urls', namespace="registration")),
    url('', include('social.apps.django_app.urls', namespace='social')),
    (r'^comments/', include('django_comments.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)