#!/bin/bash

python manage.py migrate
python manage.py collectstatic --noinput

echo Starting Gunicorn.
exec gunicorn django_default.wsgi:application \
    --name django_default \
    --bind 0.0.0.0:8001 \
    --workers 3 \
    --log-level=info \
    "$@"