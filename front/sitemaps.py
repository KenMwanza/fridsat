from django.contrib.sitemaps import Sitemap
from front.models import Business, County, Category, Area, CustomBusinessGroup

class BusinessSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1

    def items(self):
        return Business.objects.all()

class CountySitemap(Sitemap):
    changefreq = 'never'
    priority = 1

    def items(self):
        return County.objects.all()

class AreaSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1

    def items(self):
        return Area.objects.all()

class CategorySitemap(Sitemap):
    changefreq = 'monthly'
    priority = 1

    def items(self):
        return Category.objects.all()

class CustomBusinessGroupSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1

    def items(self):
        return CustomBusinessGroup.objects.all()