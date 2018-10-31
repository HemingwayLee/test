FROM java:8

RUN apt-get -qq update && apt-get install --no-install-recommends -qqy \
    curl \
    sudo

# ########## java related ##########
# RUN apt-get update && apt-get upgrade -y && apt-get install -y \
#   apt-utils \
#   software-properties-common
# RUN add-apt-repository ppa:webupd8team/java -y && apt-get update
# RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
# RUN apt-get install -y oracle-java8-installer

# ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

# RUN java -version

RUN echo "deb http://www.apache.org/dist/cassandra/debian 311x main" | sudo tee -a /etc/apt/sources.list.d/cassandra.sources.list
RUN curl https://www.apache.org/dist/cassandra/KEYS | sudo apt-key add -
#RUN sudo apt-key adv --keyserver pool.sks-keyservers.net --recv-key A278B781FE4B2BDA
RUN apt-get -qq update && apt-get install cassandra -yqq

ENTRYPOINT ["/bin/bash"]

#ref:
#http://cassandra.apache.org/download/

#How to run:
#docker run -it -p ????:???? -p ????:???? --rm my-cassandra