import os
from .base import * # noqa

DEBUG = True

ALLOWED_HOSTS = ['*']

DEV_APPS = [
    'django_extensions',
]

INSTALLED_APPS = INSTALLED_APPS + DEV_APPS
