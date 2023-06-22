#appache server
FROM php:5.6.40-apache

COPY challenge/ /var/www/html/
EXPOSE 80

RUN sed -i 's/index.html/index.php index.html/g' /etc/apache2/mods-enabled/dir.conf
RUN adduser --disabled-password --force-badname ctf
USER ctf