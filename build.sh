#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install

python manage.py tailwind install
python manage.py tailwind build

python manage.py collectstatic --no-input
python manage.py migrate
