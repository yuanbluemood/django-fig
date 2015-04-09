from centos:centos7

maintainer liuchangfu

run yum install -y gcc
run yum install -y python python-devel python-setuptools mysql-devel
run easy_install pip

ADD . /home/code
WORKDIR /home/code
RUN pip install -r requirements.txt
