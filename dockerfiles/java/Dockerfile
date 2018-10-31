FROM ubuntu:16.04

#install with oracle jdk
#RUN apt-get update && apt-get upgrade -y && apt-get install -y \
#  vim \
#  man \
#  sudo

#for add-apt-repository
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
  apt-utils \
  software-properties-common
RUN add-apt-repository ppa:webupd8team/java -y && apt-get update

RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections

RUN apt-get install -y oracle-java8-installer

#set JAVA_HOME (method 1)
#WORKDIR /etc
#RUN echo "JAVA_HOME=\"/usr/lib/jvm/java-8-oracle\"" >> environment
#RUN source /etc/environment #it doesn't work in docker RUN

#set JAVA_HOME (method 2)
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

#check installation
RUN echo $JAVA_HOME
RUN java -version

ENTRYPOINT ["/bin/bash"]
