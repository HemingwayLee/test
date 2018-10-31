FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
g++ \
vim

RUN mkdir -p /home/cpp
WORKDIR /home/cpp
COPY test.cpp /home/cpp/test.cpp

ENTRYPOINT ["/bin/bash"]

