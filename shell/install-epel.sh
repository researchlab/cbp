#!/bin/sh
echo "download aliyun repo"
wget http://mirrors.aliyun.com/repo/Centos-7.repo /etc/yum.repos.d/centos-7-aliyun.repo
echo "make env"
yum clean all && yum makecache
echo "install epel-release"
yum install -y epel-release
