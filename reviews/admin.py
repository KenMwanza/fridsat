from django.contrib import admin
from reviews.models import Vote

class VoteAdmin(admin.ModelAdmin): pass
admin.site.register(Vote, VoteAdmin)
