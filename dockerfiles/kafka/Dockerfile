FROM ubuntu:16.04

RUN apt-get update && apt-get install -y vim

# install Java
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
  apt-utils \
  net-tools \
  software-properties-common
RUN add-apt-repository ppa:webupd8team/java -y && apt-get update

RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections

# must be java8, not java7
RUN apt-get install -y oracle-java8-installer

# install kafka
RUN apt-get install -y zookeeperd

# Install and Start Kafka Server
RUN wget "http://www-eu.apache.org/dist/kafka/1.1.0/kafka_2.11-1.1.0.tgz"

RUN mkdir /opt/Kafka
RUN tar -xvf kafka_2.11-1.1.0.tgz -C /opt/Kafka/

# Run zookeeper
# service zookeeper start

# Run Kafka
# /opt/Kafka/kafka_2.11-1.1.0/bin/kafka-server-start.sh /opt/Kafka/kafka_2.11-1.1.0/config/server.properties

# Run Kafka in the background
# nohup /opt/Kafka/kafka_2.11-1.1.0/bin/kafka-server-start.sh /opt/Kafka/kafka_2.11-1.1.0/config/server.properties &

# test kafka server
# /opt/Kafka/kafka_2.11-1.1.0/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1  --partitions 1 --topic testing

ENTRYPOINT ["/bin/bash"]


# we can check java version by
# sudo java -version
# echo $JAVA_HOME

# test by running the following command
#netstat -ant | grep :2181

# Ref:
# https://devops.profitbricks.com/tutorials/install-and-configure-apache-kafka-on-ubuntu-1604-1/
