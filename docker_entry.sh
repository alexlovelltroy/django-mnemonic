#!/bin/bash
python manage.py migrate                  # Apply database migrations
python manage.py collectstatic --noinput  # Collect static files

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn mnemonic.wsgi:application \
    --name mnemonic \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    "$@"
