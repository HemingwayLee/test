FROM ubuntu:16.04

#https://hub.docker.com/r/pallet/git-client/~/dockerfile/
RUN apt-get -qq update && apt-get install --no-install-recommends -qqy \
    curl \
    ca-certificates \
    git \
    openssh-client

RUN git config --global user.name "ywlee"
RUN git config --global user.email "ywlee@vauldex.com"

RUN mkdir -p ~/.ssh
RUN chmod 700 ~/.ssh
#RUN cd ~/.ssh
#RUN touch ~/.ssh/config
#RUN chmod 600 ~/.ssh/config

RUN mkdir -p /home/kenny
COPY id_rsa /home/kenny/id_rsa
RUN cp /home/kenny/id_rsa ~/.ssh/id_rsa
COPY id_rsa.pub /home/kenny/id_rsa.pub
RUN cp /home/kenny/id_rsa.pub ~/.ssh/id_rsa.pub
COPY config /home/kenny/config
RUN cp /home/kenny/config ~/.ssh/config

ENTRYPOINT ["/bin/bash"]

#git clone ssh://git@git.vaultedman.com:56699/rejima/mrid-lib.git
