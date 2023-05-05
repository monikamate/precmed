from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_dxvam^3-t)7te(1tim+e@xuv=ionnl@v*+an1bdks$zshwq#8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'precmed',
        'HOST': 'localhost',
        'USER' : 'root',
        'PASSWORD' : 'zeon@123'
    }
}