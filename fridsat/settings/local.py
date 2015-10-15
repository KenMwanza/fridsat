"""
Django settings for fridsat project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# -*- coding: utf-8 -*-
gettext = lambda s: s

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Additional location of templates folder 
from os.path import join

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')l!s=672)fx%@i+n72!d11wqkk)9f7z&r9we88div@5vy3i!lz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

LOGIN_REDIRECT_URL = '/home'


# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.flatpages',
    'haystack',
    'taggit',
    'front',
    'cms',
    'mptt',
    'menus',
    'sekizai',
    'djangocms_admin_style',
    'treebeard',
    'registration',
    'reviews',
    'django.contrib.admin',
    'social.apps.django_app.default',
    'django_comments',
    'reversion',
    'easy_thumbnails',
    'filer',
    'djangocms_picture',
    'djangocms_text_ckeditor',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.debug',
                'django.core.context_processors.i18n',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.core.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                #'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
                'django.template.context_processors.request',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
                'front.context_processors.categories_processor',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    #'social.pipeline.social_auth.associate_by_email',
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOAuth2',
    #'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
)
# Social auth settings
#SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

COMMENTS_APP = 'reviews'

SITE_ID = 1

# Config settings
from config import *

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.admindocs.middleware.XViewMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

# Custom MIDDLEWARE_CLASSES
MIDDLEWARE_CLASSES += ('django.contrib.flatpages.middleware.FlatpageFallbackMiddleware', )

ROOT_URLCONF = 'fridsat.urls'

WSGI_APPLICATION = 'fridsat.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fridsatdb',
        'USER': 'fridsat',
        'PASSWORD': 'fridsat',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

# Search

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
        'TIMEOUT': 60,
        # ...or for multicore...
        # 'URL': 'http://127.0.0.1:8983/solr/mysite',
    },
}

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# For Django-CMS

MIGRATION_MODULES = {
    'cms': 'cms.migrations_django',
    'menus': 'menus.migrations_django',
}

CMS_TEMPLATES = (
    ('cms/template_1.html', 'Template One'),
)

LANGUAGES = [
  ('en-us', 'English'),
]

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'