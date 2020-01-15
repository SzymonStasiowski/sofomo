web: python manage.py collectstatic --noinput
web: gunicorn sofomo.wsgi
web: python manage.py runserver 0.0.0.0:$PORT