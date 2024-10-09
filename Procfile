release: python manage.py collectstatic --noinput
release: python manage.py migrate --noinput

web: gunicorn personasite.wsgi:application
