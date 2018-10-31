FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
sudo \
man \
vim

RUN mkdir -p /home/shell
WORKDIR /home/shell
COPY hello.sh /home/shell/hello.sh
RUN chmod 777 hello.sh
RUN ./hello.sh mysql

ENTRYPOINT ["/bin/bash"]
