FROM ubuntu:16.04


RUN apt-get update && apt-get install -yqq ruby rubygems-integration apt-utils

# install fake-s3
RUN gem install fakes3

# run fake-s3
RUN mkdir -p /fakes3_root
#ENTRYPOINT ["/usr/local/bin/fakes3"]
#CMD ["-r",  "/fakes3_root", "-p",  "4569"]
#EXPOSE 4569


ENTRYPOINT /usr/local/bin/fakes3 -r /fakes3_root -p 4567 && /bin/bash

#docker run -it -p 4567:4567 --rm my-test-linux

#ref:
#https://github.com/jubos/fake-s3
