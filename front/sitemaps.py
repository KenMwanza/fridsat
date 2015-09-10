from django.contrib.sitemaps import Sitemap
from front.models import Business, County, Category

class BusinessSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1

    def items(self):
        return Business.objects.all()

    def lastmod(self, obj):
        return obj.pub_date

class CountySitemap(Sitemap):
    changefreq = 'never'
    priority = 1

    def items(self):
        return County.objects.all()

class CategorySitemap(Sitemap):
    changefreq = 'never'
    priority = 1

    def items(self):
        return Category.objects.all()