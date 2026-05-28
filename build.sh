#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --noinput --settings=restaurant_kitchen_service.settings.prod
python manage.py migrate --settings=restaurant_kitchen_service.settings.prod
