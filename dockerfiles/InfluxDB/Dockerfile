FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
    curl \
    wget \
    vim \
    sudo

RUN wget https://dl.influxdata.com/influxdb/releases/influxdb_1.4.2_amd64.deb
RUN sudo dpkg -i influxdb_1.4.2_amd64.deb

# another way to install, but no `influx` cli tool:
# RUN curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -
# #source: command not found
# #RUN sudo source /etc/lsb-release
# RUN /bin/bash -c "source /etc/lsb-release"
# RUN echo "deb https://repos.influxdata.com/${DISTRIB_ID,,} ${DISTRIB_CODENAME} stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
# RUN apt-get update && sudo apt-get install influxdb

#How to run:
#influxd
#How to run in the background:
#nohup influxd > /dev/null 2>&1 &

#Command line:
#influx

#check config:
#influxd config

ENTRYPOINT ["/bin/bash"]

#create database mydb
#show databases
#use mydb
#insert cpu,host=server1,location=us-west value=10
#insert cpu,host=server1,location=japan value=11
#insert cpu,host=server2,location=us-west value=12
#select * from cpu
#show series
#show measurements

#ref:
#https://docs.influxdata.com/influxdb/v1.4/introduction/installation/

#How to run:
#docker run -it -p 8086:8086 -p 8088:8088 --rm my-influxdb




#note
# A single measurement can belong to different retention policies. A retention policy describes how long InfluxDB keeps data (DURATION) and how many copies of those data are stored in the cluster (REPLICATION)

# A series is the collection of data that share a retention policy, measurement, and tag set.

# A point is the field set in the same series with the same timestamp. 

# InfluxDB can use different storage engines (LevelDB, RocksDB, HyperLevelDB, and LMDB) for the underlying storage of data. 
