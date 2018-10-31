FROM ubuntu:16.04

#https://hub.docker.com/r/pallet/git-client/~/dockerfile/
RUN apt-get -qq update && apt-get install --no-install-recommends -qqy \
    curl \
    ca-certificates \
    git \
    openssh-client \
    postgresql \
    postgresql-contrib \
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


########## git related ##########
RUN git config --global user.name "ywlee"
RUN git config --global user.email "ywlee@vauldex.com"

RUN mkdir -p ~/.ssh
RUN chmod 700 ~/.ssh
#RUN cd ~/.ssh
#RUN touch ~/.ssh/config
#RUN chmod 600 ~/.ssh/config

RUN mkdir -p /home/kenny
COPY id_rsa /home/kenny/id_rsa
RUN cp /home/kenny/id_rsa ~/.ssh/id_rsa
COPY id_rsa.pub /home/kenny/id_rsa.pub
RUN cp /home/kenny/id_rsa.pub ~/.ssh/id_rsa.pub
COPY config /home/kenny/config
RUN cp /home/kenny/config ~/.ssh/config


########## psql related ##########
WORKDIR /etc/postgresql/9.5/main
RUN sed -i 's/#listen_addresses/listen_addresses/g' postgresql.conf
RUN sed -i 's/localhost/\x2A/g' postgresql.conf
RUN echo "host    all             all              0.0.0.0/0               trust" >> pg_hba.conf
RUN echo "host    all             all              ::/0                    trust" >> pg_hba.conf


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


ENTRYPOINT /etc/init.d/postgresql restart && /bin/bash

#git clone ssh://git@git.vaultedman.com:56699/mrexchange/mrid-api.git
#git clone ssh://git@git.vaultedman.com:56699/rejima/mrid-lib.git
