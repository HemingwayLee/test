FROM ubuntu:16.04

#install multiple package
RUN apt-get update && apt-get install -y \
man \
vim \
sudo \
wget \
net-tools

#for add-apt-repository
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
  apt-utils \
  software-properties-common
RUN add-apt-repository ppa:webupd8team/java -y && apt-get update

RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections

RUN apt-get install -y oracle-java8-installer

ENV JAVA_HOME /usr/lib/jvm/java-8-oracle


WORKDIR usr/local/
RUN wget https://archive.apache.org/dist/hbase/hbase-0.98.8/hbase-0.98.8-hadoop2-bin.tar.gz
RUN tar -zxvf hbase-0.98.8-hadoop2-bin.tar.gz
#RUN mv hbase-0.99.1/* HBase/
RUN mv hbase-0.98.8-hadoop2 HBase

WORKDIR /usr/local/HBase/conf
RUN echo "export JAVA_HOME=/usr/lib/jvm/java-8-oracle" >> hbase-env.sh

COPY hbase-site.xml /usr/local/HBase/conf/hbase-site.xml
RUN /usr/local/HBase/bin/start-hbase.sh

ENTRYPOINT /usr/local/HBase/bin/hbase shell && /bin/bash

#./hbase-daemon.sh start rest

#https://www.tutorialspoint.com/hbase/hbase_shell.htm
#https://archive.apache.org/dist/hbase/hbase-0.98.8/


#TODO:
#https://stackoverflow.com/questions/25069084/how-can-i-make-hbase-region-server-listen-on-0-0-0-0
