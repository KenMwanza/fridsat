from django.contrib import admin
from front.models import Business, County, Category, Area

admin.site.register(County)
admin.site.register(Area)
admin.site.register(Business)
admin.site.register(Category)