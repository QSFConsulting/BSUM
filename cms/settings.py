from base import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

ALLOWED_HOSTS = ['188.166.28.185', '188.166.37.173', '.bsum.fi']

DEBUG = False

TEMPLATE_DEBUG = False

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'YK4GLHm24o',
        'HOST': 'localhost',
        'PORT': '',
    }
}


STATIC_URL = '/static/'
STATICFILES_DIRS = (
    "/home/django/django_project/cms/static",
)
STATIC_ROOT = "/var/www/bsumfi/static/"
