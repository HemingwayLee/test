FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
nodejs \
npm \
vim

RUN mkdir -p /home/insight

#we can't install insight-api without bitcore
#RUN npm install -g bitcore-node@latest
#RUN bitcore-node create mynode


ENTRYPOINT ["/bin/bash"]
