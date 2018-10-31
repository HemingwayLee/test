FROM ubuntu:16.04

#install multiple package
RUN apt-get update && apt-get install -y \
nodejs \
npm \
man \
vim

RUN mkdir -p /home/hello
WORKDIR /home/hello
RUN npm install -g browserify
RUN npm install uniq

#browserify calls nodejs with command "node", create a symlink from nodejs to node with
RUN ln -s `which nodejs` /usr/bin/node

#make hello.js
RUN echo "var unique = require('uniq');" >> hello.js
RUN echo "var data = [1, 2, 2, 3, 4, 5, 5, 5, 6];" >> hello.js
RUN echo "console.log(unique(data));" >> hello.js

RUN browserify hello.js -o bundle.js


ENTRYPOINT ["/bin/bash"]

#check npm installation
#npm ls -g | grep "browserify"

#copy result from container to host
#docker cp 8174ef74cd02:/home/hello/bundle.js bundle.js


#ref
#http://browserify.org/
