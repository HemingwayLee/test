FROM ubuntu:16.04

#install multiple package
RUN apt-get update && apt-get install -y \
nodejs \
npm \
man \
vim \
sudo \
curl \
ca-certificates \
git \
openssh-client

RUN mkdir -p /home/hello
WORKDIR /home/hello
RUN echo "console.log('Hello, World');" > hello.js
#node hello.js

#Since fsevents is an API in OS X, we don't need it
#RUN npm install -g fsevents

#DataApi calls nodejs with command "node", create a symlink from nodejs to node with
RUN sudo ln -s `which nodejs` /usr/bin/node

RUN npm install -g --no-optional chokidar
RUN git clone https://github.com/ripple/rippled-historical-database.git
WORKDIR /home/hello/rippled-historical-database
RUN npm install


ENTRYPOINT ["/bin/bash"]
