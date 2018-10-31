FROM ubuntu:16.04

#install multiple package
RUN apt-get update && apt-get install -y \
ssh \
python \
python-pip \
python-virtualenv \
wget \
unzip \
vim

RUN mkdir -p /home/aws
WORKDIR /home/aws
RUN wget https://s3.amazonaws.com/aws-cli/awscli-bundle.zip
RUN unzip awscli-bundle.zip
RUN ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws

RUN printf "AKIAJJWXTWUK72UKO3ZA\nku240YOE98NEghG7pwaTNiNxJges8YmQmGoyrQNr\nus-east-1\njson" | aws configure

#RUN printf "{Access Key ID}\n{Secret Access Key}\nus-east-1\njson" | aws configure

#RUN aws s3 ls

ENTRYPOINT ["/bin/bash"]

#aws s3 ls
#aws s3 mb s3://script-runner-test
#echo "hello s3" > hello.txt
#aws s3 cp hello.txt s3://script-runner-test
#aws s3 ls s3://script-runner-test
#aws s3 cp s3://script-runner-test/hello.txt - (showing the content)
#aws s3 rb s3://script-runner-test
#aws s3 rb s3://script-runner-test --force (if file exists on s3)



#aws ec2 describe-regions (output will be json format by configuration)
#aws ec2 describe-regions --output table (output will be table format)
#aws ec2 describe-instances --instance-ids i-0bf5dfbf08016c1c9
#aws ec2 describe-key-pairs
#aws ec2 describe-security-groups --group-ids sg-cc80aeb0
#aws ec2 run-instances --image-id ami-cd0f5cb6 --count 1 --instance-type t2.micro --key-name ywlee --security-groups "ALL TRAFFIC"


#michael centos AMI: ami-62c6c074
#default ubuntu AMI: ami-cd0f5cb6

#aws rds create-db-instance --db-instance-identifier mold-coin-test --allocated-storage 5 --db-instance-class db.t2.small --engine postgres --master-username root --master-user-password rootroot

#need to change the security group on AWS to open the port...
#connect
#psql -h mold-coin-test.cduvdyp1klg4.us-east-1.rds.amazonaws.com -p 5432 -U root postgres



#copy file into docker
#docker cp ad3.jpeg {container id}:/ad3.jpeg
#docker cp ad3.jpeg 5032bbfae1f9:/ad3.jpeg


#ref:
#https://aws.amazon.com/tw/cli/
#https://www.youtube.com/watch?v=FwbavIglhis
#http://docs.aws.amazon.com/cli/latest/userguide/cli-ec2-launch.html
