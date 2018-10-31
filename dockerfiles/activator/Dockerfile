FROM ubuntu:16.04

RUN apt-get -qq update && apt-get install --no-install-recommends -qqy \
    wget \
    unzip \
    vim

########## java related ##########
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
  apt-utils \
  software-properties-common
RUN add-apt-repository ppa:webupd8team/java -y && apt-get update
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
RUN apt-get install -y oracle-java8-installer

ENV JAVA_HOME /usr/lib/jvm/java-8-oracle


########## activator related ##########
#change the version in the future?
ENV SCALA_VERSION 2.12.1
ENV ACTIVATOR_VERSION 1.2.12

RUN apt-get remove scala-library scala && \
    wget http://www.scala-lang.org/files/archive/scala-$SCALA_VERSION.deb && \
    dpkg -i scala-$SCALA_VERSION.deb  && \
    apt-get update && \
    apt-get install scala && \
    rm scala-$SCALA_VERSION.deb
RUN cd /tmp && \
    wget http://downloads.typesafe.com/typesafe-activator/$ACTIVATOR_VERSION/typesafe-activator-$ACTIVATOR_VERSION.zip && \
    unzip typesafe-activator-$ACTIVATOR_VERSION.zip -d /usr/local && \
    mv /usr/local/activator-$ACTIVATOR_VERSION /usr/local/activator && \
    rm typesafe-activator-$ACTIVATOR_VERSION.zip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    echo 'export PATH=$PATH:/usr/local/activator' >> /root/.bashrc


ENTRYPOINT ["/bin/bash"]
