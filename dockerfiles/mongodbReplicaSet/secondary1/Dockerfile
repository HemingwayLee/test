FROM ubuntu:16.04

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927

RUN echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list

RUN apt-get update && apt-get install -y mongodb-org

RUN sed -i 's/  bindIp: 127.0.0.1/  bindIp: 0.0.0.0/g' /etc/mongod.conf

RUN mkdir -p /data/db

ENTRYPOINT ["/bin/bash"]

#run mongod inside docker
#mongod --replSet "rs0"

#run mongod in the background
#nohup mongod --replSet "rs0" > /dev/null 2>&1 &

#docker build -t my-mongo2 .
#docker run --net mynet123 --ip 172.18.0.14 -it --rm -p 30002:27017 my-mongo2
