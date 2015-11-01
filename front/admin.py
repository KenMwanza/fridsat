from django.contrib import admin
from front.models import Business, County, Category, Area, CustomBusinessGroup

admin.site.register(County)
admin.site.register(Area)
admin.site.register(Business)
admin.site.register(Category)
admin.site.register(CustomBusinessGroup)