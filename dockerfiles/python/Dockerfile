FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
  python3 \
  python3-pip \
  python3-venv

# python3 -m venv my_environment
# source my_environment/bin/activate
# pip3 install numpy
# pip3 list
# deactivate
# pip3 list

RUN echo 'print("print from python")' > test.py
RUN python3 test.py

ENTRYPOINT ["/bin/bash"]
