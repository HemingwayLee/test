FROM ubuntu:16.04

#install multiple package
RUN apt-get update && apt-get install -y \
man \
vim \
net-tools \
postfix \
iputils-ping

#RUN newaliases


#RUN postconf -e 'home_mailbox= Maildir/'

#RUN postfix start

ENTRYPOINT /etc/init.d/postfix start && /bin/bash


#Ref:
#http://www.samlogic.net/articles/smtp-commands-reference.htm
#http://linux.vbird.org/linux_server/0380mail.php#postfix
#https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-postfix-on-ubuntu-16-04

#HELO 127.0.0.1
#MAIL FROM: ywlee@153.126.131.176
#RCPT TO: ywlee@153.126.131.176
#DATA
#Hi gogog
#.

