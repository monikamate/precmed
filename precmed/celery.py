import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','precmed.settings.dev')

celery = Celery('precmed')

celery.config_from_object('django.conf:settings', namespace='CELERY')
celery.autodiscover_tasks()