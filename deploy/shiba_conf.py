# -*- coding: utf-8 -*-

VERSION = '{{ code_version }}'

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['*']

# Static files for nginx
STATIC_URL = '{{ django_static_url }}'
STATIC_ROOT = '{{ django_static_root }}'
MEDIA_URL = '{{ django_media_url }}'
MEDIA_ROOT = '{{ django_media_root }}'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '{{ mysql_name }}',
        'USER': '{{ mysql_user }}',
        'PASSWORD': '{{ mysql_password }}',
        'HOST': '{{ mysql_host }}',
        'PORT': '{{ mysql_port }}',
    }
}

# Logging
# LOGGING_FILE = '{{ app_log_dir_path }}/django.log'

# Page limit
PAGE_LIMIT = 10
