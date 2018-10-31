FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
  vim \
  net-tools \
  zookeeperd 

# Run zookeeper
# service zookeeper start

ENTRYPOINT ["/bin/bash"]

# 
# service zookeeper {start|stop|status|restart|force-reload}

# Ref:
# https://medium.com/@ryannel/installing-zookeeper-on-ubuntu-9f1f70f22e25