FROM ubuntu:16.04

RUN apt-get update && apt-get install -yqq \
  cron \
  vim

RUN mkdir -p /home/test
WORKDIR /home/test

RUN echo "echo 'hello schedule' >> /home/test/result.log" > hello.sh
RUN chmod 777 hello.sh

RUN echo 'cronjob="* * * * * /home/test/hello.sh"' > addJob.sh
RUN echo '(crontab -u root -l; echo "$cronjob" ) | crontab -u root -' >> addJob.sh
RUN chmod 777 addJob.sh
RUN ./addJob.sh

RUN crontab -l

ENTRYPOINT ["/bin/bash"]


#service cron start

#open text editor and add a job manually
#crontab -e

#check the jobs
#crontab -l
