FROM ubuntu:16.04

RUN mkdir -p /home/test
WORKDIR /home/test
RUN echo "echo 'Hello, world'" > hello.sh
RUN echo "exec '$@'" > hello.sh
RUN chmod 777 hello.sh

#ENTRYPOINT ["/bin/bash"]

#not successful
ENTRYPOINT ["/home/test/hello.sh"]
