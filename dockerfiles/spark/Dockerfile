FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
  curl \
  vim \
  git

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
  apt-utils \
  software-properties-common
RUN add-apt-repository ppa:webupd8team/java -y && apt-get update

RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections

#must be java8, not java7
RUN apt-get install -y oracle-java8-installer

RUN mkdir -p /usr/local/share/spark
WORKDIR /usr/local/share/spark

RUN curl http://d3kbcqa49mib13.cloudfront.net/spark-2.0.2.tgz | tar xvz -C /usr/local/share/spark
WORKDIR /usr/local/share/spark/spark-2.0.2

RUN ./build/mvn -DskipTests clean package

RUN ./bin/run-example SparkPi 10

ENTRYPOINT ["/bin/bash"]

#ref:
#http://blog.prabeeshk.com/blog/2016/12/07/install-apache-spark-2-on-ubuntu-16-dot-04-and-mac-os/
