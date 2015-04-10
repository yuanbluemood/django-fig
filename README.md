使用fig+docker搭建基于django+mysql的web开发环境
==================================

django单独用基于centos7，安装python相关环境，注意mysql-devel的安装，否则连db会报错，
django及相关包写入requirements.txt，采用pip安装
 Dockerfile如下：

from centos:centos7

maintainer liuchangfu

run yum install -y gcc
run yum install -y python python-devel python-setuptools mysql-devel
run easy_install pip

ADD . /home/code
WORKDIR /home/code
RUN pip install -r requirements.txt




参考资料：
http://yeasy.gitbooks.io/docker_practice/content/fig/django.html
https://registry.hub.docker.com/_/mysql/
https://docs.djangoproject.com/en/1.8/ref/contrib/admin/
https://github.com/yuanbluemood


使用fig run web startproject YOURPROJECT-NAME . 在当前目录生成django项目
修改setting.py中的DB设置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cmsm',
        'USER': 'user',
        'PASSWORD': 'userpasswd',
        'HOST': 'db',
        'PORT': '3306',
    }
}



##fig install参考如下，直接curl下载安装
http://yeasy.gitbooks.io/docker_practice/content/fig/install.html
#fig build
#fig up
