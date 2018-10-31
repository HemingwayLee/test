FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
  nodejs \
  npm \
  vim

RUN mkdir -p /home/hello
WORKDIR /home/hello
RUN npm install marked
WORKDIR /home/hello/node_modules/marked

ENTRYPOINT ["/bin/bash"]

#copy result from contain to host
#docker cp aff4a96eaf92:/home/hello/node_modules/marked/marked.min.js marked.min.js

