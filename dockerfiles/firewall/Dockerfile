FROM ubuntu:16.04

#install multiple package
RUN apt-get update && apt-get install -y \
man \
vim \
openssh-server \
net-tools \
ufw

#because of the privileged, we can not run it here..
#RUN ufw enable
#RUN ufw default deny incoming
#RUN ufw allow 22

ENTRYPOINT ["/bin/bash"]


#it should run in privileged mode
#docker run --privileged -it --rm my-test-linux


#Reference:
#https://www.peterdavehello.org/2016/01/ubuntu-based-gnulinux-firewall-ufw-essential-config/
#https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-14-04
