FROM python:3.7

RUN apt-get update && apt-get install -y gettext

WORKDIR /usr/src/app/
ADD . ./ ./
RUN pip install -r requirements.txt

RUN chown -R www-data:www-data /usr/src/app/static
RUN chown -R www-data:www-data /usr/src/app/media
