FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
    default-jdk \
    wget \
    net-tools \
    openssh-server \
    vim

RUN wget http://www-eu.apache.org/dist/hadoop/common/hadoop-2.7.6/hadoop-2.7.6.tar.gz 
RUN tar -xzvf hadoop-2.7.6.tar.gz
RUN mv hadoop-2.7.6 /usr/local/hadoop

WORKDIR /usr/local/hadoop

RUN sed -i 's#export JAVA_HOME=${JAVA_HOME}#export JAVA_HOME=$(readlink -f /usr/bin/java | sed "s:bin/java::")#g' /usr/local/hadoop/etc/hadoop/hadoop-env.sh

# change settings
# etc/hadoop/core-site.xml
RUN sed -i "20i <property>" etc/hadoop/core-site.xml
RUN sed -i "21i <name>fs.defaultFS</name>" etc/hadoop/core-site.xml
RUN sed -i "22i <value>hdfs://localhost:9000</value>" etc/hadoop/core-site.xml  
RUN sed -i "23i </property>" etc/hadoop/core-site.xml

# etc/hadoop/hdfs-site.xml
RUN sed -i "20i <property>" etc/hadoop/hdfs-site.xml
RUN sed -i "21i <name>dfs.replication</name>" etc/hadoop/hdfs-site.xml
RUN sed -i "22i <value>1</value>" etc/hadoop/hdfs-site.xml      
RUN sed -i "23i </property>" etc/hadoop/hdfs-site.xml

RUN bin/hdfs namenode -format

# ssh localhost related settings
RUN ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
RUN cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
RUN chmod 0600 ~/.ssh/authorized_keys

# Run
RUN /etc/init.d/ssh start
RUN sbin/start-dfs.sh

ENTRYPOINT ["/bin/bash"]

# Check HDFS with UI:
# http://localhost:50070/

# Ref
# https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/SingleCluster.html#Pseudo-Distributed_Operation

# Run
# docker run -it --rm -p 50070:50070  my-hadoop
 
# ls
# bin/hadoop fs -ls /

# mkdir
# bin/hdfs dfs -mkdir /user
# bin/hadoop fs -mkdir /myData

# put file into hadoop file system
# bin/hadoop fs -put testfile.txt /myData

# get file from hadoop file system
# bin/hadoop fs -get /myData/testfile.txt newText.txt
