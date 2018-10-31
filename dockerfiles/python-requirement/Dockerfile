FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
  python3 \
  python3-pip \
  python3-venv

RUN echo 'nltk==3.3' > requirement.txt
RUN echo 'numpy>=1.14' >> requirement.txt

RUN pip3 install -r requirement.txt

ENTRYPOINT ["/bin/bash"]
