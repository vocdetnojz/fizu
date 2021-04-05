release: python manage.py migrate

web: gunicorn fizu.wsgi --log-file -

worker: python manage.py rqworker default
