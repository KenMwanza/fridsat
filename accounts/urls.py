from django.conf.urls import patterns, url
from django.contrib.auth.forms import SetPasswordForm
from accounts import views

urlpatterns = patterns('',
    url(r'^login/$', 'accounts.views.login', name='login'),
    url(r'^logout/$', 'accounts.views.logout', name='logout'),
    url(r'^password_change/$',  # hijack password_change's url
        'django.contrib.auth.views.password_change',
        {'password_change_form': SetPasswordForm},
        name="password_change"),
)
