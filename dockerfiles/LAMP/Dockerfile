FROM ubuntu:16.04

RUN apt-get update && apt-get install -y apache2

RUN { \
        echo debconf debconf/frontend select Noninteractive; \
        echo mysql-community-server mysql-community-server/data-dir \
            select ''; \
        echo mysql-community-server mysql-community-server/root-pass \
            password '10321032'; \
        echo mysql-community-server mysql-community-server/re-root-pass \
            password '10321032'; \
        echo mysql-community-server mysql-community-server/remove-test-db \
            select true; \
    } | debconf-set-selections \
    && apt-get update && apt-get install -y mysql-server

RUN apt-get update && apt-get install -y \
php \
libapache2-mod-php \
php-mcrypt \
php-mysql

WORKDIR /var/www/html/
RUN echo "<?php echo 'hello, php!' ?>" > hello.php

ENTRYPOINT /etc/init.d/apache2 start && /bin/bash
