FROM ubuntu:16.04


RUN apt-get update && apt-get install -y \
vim \
apache2 \
net-tools

WORKDIR /var/www/html/
RUN echo "<html><body><h1>Hello, Apache</h1></body></html>" > hello.html

ENTRYPOINT /etc/init.d/apache2 start && /bin/bash
