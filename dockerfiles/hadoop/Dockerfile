FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
    default-jdk \
    wget \
    vim

RUN wget http://www-eu.apache.org/dist/hadoop/common/hadoop-2.7.6/hadoop-2.7.6.tar.gz 
RUN tar -xzvf hadoop-2.7.6.tar.gz
RUN mv hadoop-2.7.6 /usr/local/hadoop

WORKDIR /usr/local/hadoop

#RUN readlink -f /usr/bin/java | sed "s:bin/java::"

#Use Readlink to Set the Value Dynamically
RUN sed -i 's#export JAVA_HOME=${JAVA_HOME}#export JAVA_HOME=$(readlink -f /usr/bin/java | sed "s:bin/java::")#g' /usr/local/hadoop/etc/hadoop/hadoop-env.sh

RUN mkdir ~/input
RUN cp /usr/local/hadoop/etc/hadoop/*.xml ~/input

#Run map reduce
RUN /usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.6.jar grep ~/input ~/grep_example 'principal[.]*'
#Get the result
RUN cat ~/grep_example/*

ENTRYPOINT ["/bin/bash"]

#ref:
#https://www.digitalocean.com/community/tutorials/how-to-install-hadoop-in-stand-alone-mode-on-ubuntu-16-04
