FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
  vim \
  python2.7 \
  wget \
  net-tools

#get latest version of rabbitmq
RUN echo "deb http://www.rabbitmq.com/debian/ testing main" >> /etc/apt/sources.list
RUN wget http://www.rabbitmq.com/rabbitmq-signing-key-public.asc
RUN apt-key add rabbitmq-signing-key-public.asc

RUN apt-get update && apt-get install -y --allow-unauthenticated rabbitmq-server

#enable web management tool
RUN rabbitmq-plugins enable rabbitmq_management

#Can not use systemctl
#systemctl enable rabbitmq-server
#systemctl start rabbitmq-server

#TODO: use python code to test it...
#RUN echo 'print("print from python")' > test.py
#RUN python2.7 test.py

ENTRYPOINT /etc/init.d/rabbitmq-server start && /bin/bash


#ref:
# docker run -it --rm -p 15672:15672 my-test-linux
# http://127.0.0.1:15672/api
# http://127.0.0.1:15672/
# http://blog.topspeedsnail.com/archives/4750
