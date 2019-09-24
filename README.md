# Taking your API to the next level - DjangoCon2019

<p align="center">
  <img src="https://s3.amazonaws.com/carlosmart.co/talks/images/djangocon.png">
</p>

### Django examples
* django cache
* django select_related
* django prefetch_related

### This project use this tools:
* django-cacheops
* django-url-filter
* drf-renderer-xlsx
* dry-rest-permissions

## Run this project
This project uses docker to run in different environments:

* Install docker
* Clone repo
* run `docker-compose up`

### Init project with example data
* run `docker exec -it 5minutes_api_five_minutes_1 bash`
* Then you can type one of the following commands
    * `python manage.py init_project` Init with small set of data `usr: admin@admin.co`, `pass: 123admin123`
    * `python manage.py create_tickets 5000` Creates tickets you can replace 5000 with any number
    * `python manage.py invalidate_cache` Invalidates cache for `event_list` view.