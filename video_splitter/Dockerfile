FROM python:3.8.20

RUN apt-get update &&  apt-get install -y ffmpeg

RUN mkdir -p /home/proj/
COPY . /home/proj/
WORKDIR /home/proj/

RUN pip3 install -r requirements.txt

