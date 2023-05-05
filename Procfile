release: python manage.py migrate
web: gunicorn precmed.wsgi
worker: celery -A precmed worker
