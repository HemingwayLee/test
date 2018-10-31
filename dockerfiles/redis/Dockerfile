FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
curl \
build-essential tcl

RUN mkdir -p /home/test

#cd will not work, use WORKDIR
#RUN cd /home/test
WORKDIR /home/test

RUN curl -O http://download.redis.io/redis-stable.tar.gz
RUN tar xzvf redis-stable.tar.gz
WORKDIR /home/test/redis-stable
RUN make
RUN make test
RUN make install

RUN mkdir /etc/redis
RUN cp /home/test/redis-stable/redis.conf /etc/redis

WORKDIR /etc/redis
RUN sed -i 's/supervised no/supervised systemd/g' redis.conf

#https://stackoverflow.com/questions/12061410/how-to-replace-a-path-with-another-path-in-sed
RUN sed -i 's#dir ./#dir /var/lib/redis#g' redis.conf
RUN sed -i 's/bind 127.0.0.1/bind 0.0.0.0/g' redis.conf

COPY redis.service /etc/systemd/system/redis.service

RUN adduser --system --group --no-create-home redis
RUN mkdir /var/lib/redis
RUN chown redis:redis /var/lib/redis   # make redis own /var/lib/redis
RUN chmod 770 /var/lib/redis           # adjust permission

#run redis in the background
#nohup /usr/local/bin/redis-server /etc/redis/redis.conf > /dev/null 2>&1 &

ENTRYPOINT ["/bin/bash"]

#ENTRYPOINT ["/usr/local/bin/redis-server"]
#CMD ["/etc/redis/redis.conf"]


#docker run -it --rm -p 6379:6379 my-test-linux


#ref:
#https://askubuntu.com/questions/868848/how-to-install-redis-on-ubuntu-16-04
#https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-redis-on-ubuntu-16-04

