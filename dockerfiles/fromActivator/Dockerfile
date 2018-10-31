FROM my-test-linux

RUN apt-get update && apt-get install -y \
nginx \
vim \
net-tools

#change the nginx config
WORKDIR /etc/nginx/sites-enabled
#insert config
RUN sed -i '16 i\upstream vauldex-web {' default
RUN sed -i '17 i\  server 127.0.0.1:9000;' default
RUN sed -i '18 i\}' default
RUN sed -i '19 i\ ' default
RUN sed -i '48 i\                proxy_pass  http://vauldex-web;' default


RUN mkdir -p /home/test
WORKDIR /home/test
RUN /usr/local/activator/activator new "hello" play-scala
WORKDIR /home/test/hello
RUN /usr/local/activator/activator compile
RUN /usr/local/activator/activator playGenerateSecret | tee secret.txt
#remove lines
RUN sed -i '1d' secret.txt
RUN sed -i '1d' secret.txt
RUN sed -i '2d' secret.txt
#remove chars
RUN sed -i 's/^.\{45\}//' secret.txt
RUN sed -i 's/.\{4\}$//' secret.txt
#replace with secret
RUN sed -i "s#changeme#$(/bin/cat secret.txt)#g" conf/application.conf
RUN /usr/local/activator/activator stage
RUN /usr/local/activator/activator start 9000

ENTRYPOINT /etc/init.d/nginx restart && /bin/bash

#docker build -t my-from-activator .
#docker run -it --rm -p 8899:80 my-from-activator

#config:
#/etc/nginx/sites-enabled/default
