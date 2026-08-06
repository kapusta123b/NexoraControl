#!/bin/sh

set -e

mkdir -p /app/staticfiles
chown -R nonroot:nonroot /app/staticfiles

gosu nonroot python manage.py migrate --noinput
gosu nonroot python manage.py collectstatic --noinput

exec gosu nonroot "$@"
