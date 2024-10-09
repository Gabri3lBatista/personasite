release: python manage.py collectstatic --noinput

web: gunicorn personasite.wsgi --log-file -
