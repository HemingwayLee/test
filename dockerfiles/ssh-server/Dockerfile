FROM ubuntu:16.04

#install multiple package
RUN apt-get update && apt-get install -y \
apt-utils \
man \
vim \
openssh-server \
netcat

#TODO: append a line to file
RUN echo "sshd:10.0.4.85:allow" >> /etc/hosts.allow

#this is not working, put it into ENTRYPOINT (and CMD)
#RUN /etc/init.d/ssh restart

#add a user
RUN useradd kenny
#RUN printf "10321032\n10321032" | passwd kenny
RUN echo "kenny:10321032" | chpasswd

ENTRYPOINT /etc/init.d/ssh restart && /bin/bash

#docker build -t my-test-linux .
#docker run -it --rm -p 52022:22 my-test-linux

#ssh-keygen -R "[localhost]:52022"

#ssh -p 52022 kenny@localhost

#To the particular directory (e.g., /home):
#ssh -t -p 52022 kenny@localhost "cd /home ; bash"

#Execute script:
#ssh -p 52022 kenny@localhost "echo 'Hello'"

#Execute script in .sh file:
#ssh -p 52022 kenny@localhost 'bash -s' < test.sh

#Ref:
#https://stackoverflow.com/questions/22886470/start-sshd-automatically-with-docker-container
#https://jpetazzo.github.io/2014/06/23/docker-ssh-considered-evil/
