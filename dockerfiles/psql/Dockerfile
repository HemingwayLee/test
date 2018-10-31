FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
postgresql \
postgresql-contrib \
man \
vim \
sudo \
locate \
net-tools #it has arp, ifconfig, netstat, rarp, nameif and route

#RUN sudo -u postgres createuser root
#RUN sudo -u postgres createdb root

WORKDIR /etc/postgresql/9.5/main
RUN sed -i 's/#listen_addresses/listen_addresses/g' postgresql.conf
RUN sed -i 's/localhost/\x2A/g' postgresql.conf


RUN echo "host    all             all              0.0.0.0/0               trust" >> pg_hba.conf

RUN echo "host    all             all              ::/0                    trust" >> pg_hba.conf

ENTRYPOINT /etc/init.d/postgresql restart && /bin/bash



#https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04
#http://blog.bigbinary.com/2016/01/23/configure-postgresql-to-allow-remote-connection.html
#https://www.postgresql.org/docs/9.1/static/auth-pg-hba-conf.html

#Use postgres user name to login...
#sudo -i -u postgres
#psql


#docker run -it --rm -p 15432:5432 my-test-linux
