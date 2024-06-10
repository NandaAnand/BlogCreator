#!/bin/sh

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start the server
echo "Starting server..."
exec gunicorn django_blog.wsgi:application --bind 0.0.0.0:$PORT
