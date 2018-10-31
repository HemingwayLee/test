FROM ubuntu:16.04

#https://stackoverflow.com/questions/38356219/mysql-in-docker-frozen-at-root-password-config

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
    && apt-get update && apt-get install -y \
       mysql-server \
       man \
       vim \
       net-tools #it has arp, ifconfig, netstat, rarp, nameif and route

WORKDIR /etc/mysql
RUN echo "[mysqld]" >> my.cnf
RUN echo "bind-address    = 0.0.0.0" >> my.cnf


ENTRYPOINT /etc/init.d/mysql start && /bin/bash

#we need to run manually...
#mysql_secure_installation
#y0ynnny
#mysql -u root -p
#SET GLOBAL  validate_password_policy='LOW';
#GRANT ALL ON *.* to root@'%' IDENTIFIED BY '10321032';
#FLUSH PRIVILEGES;
#service mysql restart

#docker run -it --rm -p 13306:3306 my-test-linux
#mysql --host=127.0.0.1 --port=13306 mysql -u root -p


#Ref:
#http://nst.sourceforge.net/nst/docs/faq/ch06s04.html
#https://stackoverflow.com/questions/19101243/error-1130-hy000-host-is-not-allowed-to-connect-to-this-mysql-server
#http://bbs.bestsdk.com/detail/762.html
#https://serverfault.com/questions/139323/mysql-bind-to-more-than-one-ip-address


