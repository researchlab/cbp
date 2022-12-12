#!/bin/sh
echo "download python3.8.8  to /tmp/"
wget https://www.python.org/ftp/python/3.8.8/Python-3.8.8.tgz -O /tmp/Python-3.8.8.tgz
echo "install dependencies"
yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make libffi-devel
echo "tar -zxvf"
cd /tmp/
tar -zxvf Python-3.8.8.tgz
cd Python-3.8.8
./configure prefix=/usr/local/python3
make && make install
ln -s /usr/local/python3/bin/python3.8 /usr/bin/python3
ln -s /usr/local/python3/bin/pip3.8 /usr/bin/pip3

python3 --version
pip3 --version
