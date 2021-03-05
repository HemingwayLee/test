FROM python:3.8

RUN mkdir -p /home/app
COPY . /home/app
WORKDIR /home/app

RUN pip3 install -r requirements.txt

CMD python3 hello.py

