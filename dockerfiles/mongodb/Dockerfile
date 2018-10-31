FROM ubuntu:16.04

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927

RUN echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list

RUN apt-get update && apt-get install -y \
  mongodb-org \
  vim

RUN sed -i 's/  bindIp: 127.0.0.1/  bindIp: 0.0.0.0/g' /etc/mongod.conf

RUN mkdir -p /data/db

# RUN mkdir -p /home/test
# WORKDIR /home/test
# RUN echo "nohup mongod > /dev/null 2>&1 &" > start.sh
# # RUN echo 'exec "$@"' > start.sh
# RUN chmod 777 start.sh

ENTRYPOINT ["/usr/bin/mongod"]

EXPOSE 27017

# not working...
# ENTRYPOINT ["/bin/bash"]

# EXPOSE 27017
# CMD ["/home/test/start.sh"]
# CMD ["/usr/bin/mongod"]




#run mongod inside docker
# mongod

#run mongod in the background
#nohup mongod > /dev/null 2>&1 &

#interactive mode
#docker run -it --rm -p 27017:27017 my-test-linux

#
#docker run -p 27017:27017 my-test

#detach mode
#docker run -td -p 27017:27017 my-test

#problem:
#https://github.com/Microsoft/BashOnWindows/issues/796
