from reviews.views import VoteFormView
from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^vote/$', VoteFormView.as_view(), name="vote"),
)