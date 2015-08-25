from django.conf.urls import patterns, url
from django.contrib.auth.forms import SetPasswordForm
from registration import views

urlpatterns = patterns('',
    url(r'^login/$', 'registration.views.login', name='login'),
    url(r'^promo/landing/$', 'registration.views.landing', name='landing'),
    url(r'^accounts/password-change/$',
        'django.contrib.auth.views.password_change',
        {'password_change_form': SetPasswordForm},
        name="password_change"),
)