#!/bin/sh
sleep 5s
python manage.py migrate --settings=five_minutes.settings.prod
uwsgi --ini uwsgi.ini
