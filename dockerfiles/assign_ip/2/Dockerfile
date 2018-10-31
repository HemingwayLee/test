FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
  nginx \
  iputils-ping
# we can ping 172.18.0.15

WORKDIR /var/www/html

ENTRYPOINT /etc/init.d/nginx restart && /bin/bash

#docker network create --subnet=172.18.0.0/16 mynet123
#docker build -t my-test-linux2 .
#docker run --net mynet123 --ip 172.18.0.14 -it --rm -p 8898:80 my-test-linux2

#ref:
# https://stackoverflow.com/questions/27937185/assign-static-ip-to-docker-container/35359185#35359185
