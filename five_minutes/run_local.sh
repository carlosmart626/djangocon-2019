#!/bin/sh
sleep 5s
python manage.py migrate --settings=five_minutes.settings.dev
python manage.py runserver 0.0.0.0:8080
