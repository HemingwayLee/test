FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
man \
yum-utils \
alien \
vim \
sudo \
net-tools

RUN rpm -Uvh https://mirrors.ripple.com/ripple-repo-el7.rpm
RUN yumdownloader --enablerepo=ripple-stable --releasever=el7 rippled
RUN rpm --import https://mirrors.ripple.com/rpm/RPM-GPG-KEY-ripple-release && rpm -K rippled*.rpm
RUN alien -i --scripts rippled*.rpm && rm rippled*.rpm

RUN sed -i 's/127.0.0.1/0.0.0.0/g' /opt/ripple/etc/rippled.cfg

ENTRYPOINT /opt/ripple/bin/rippled --conf=/opt/ripple/etc/rippled.cfg --start -a && /bin/bash

#ENTRYPOINT ["/bin/bash"]

#run rippled in the background
#nohup /opt/ripple/bin/rippled --conf=/opt/ripple/etc/rippled.cfg --start -a > /dev/null 2>&1 &

#check disk size
#while printf '%s ' "$(df -P / | awk 'NR==2 { print $(NF-1) }')"; do sleep 30; done



#testing:
#POST http://127.0.0.1:5005/
#{
#    "method": "server_info",
#    "params": [
#        {}
#    ]
#}

#ledger_current
#tx_history



# run
#docker run -it --rm -p 5005:5005 -p 6006:6006 my-test-linux


#ref
#https://ripple.com/build/rippled-apis/
#https://hub.docker.com/r/inmyth/rippled-ubuntu/



