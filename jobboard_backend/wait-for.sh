#!/bin/bash
set -e

# Function to check if postgres is ready
postgres_ready() {
    python << END
import sys
import os
import psycopg2
try:
    psycopg2.connect(
        dbname=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        host=os.environ['DB_HOST'],
        port=os.environ['DB_PORT']
    )
except psycopg2.OperationalError:
    sys.exit(1)
sys.exit(0)
END
}

until postgres_ready; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 2
done

>&2 echo "Postgres is up - executing migrations"
python manage.py migrate

>&2 echo "Starting Gunicorn"
exec gunicorn jobboard_backend.wsgi:application --bind 0.0.0.0:8000
