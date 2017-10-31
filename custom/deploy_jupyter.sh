#!/bin/sh

#update git
  git config --global user.email "keep.it.that.way@gmail.com"
  git config --global user.name "weihan"

apt update
#installing dependencies
apt install -y python3
apt install -y python3-pip
apt install -y whois
pip3 install jupyterhub
apt-get install -y npm nodejs-legacy
npm install -g configurable-http-proxy
pip3 install notebook


# adding custom authentication hook
cp /root/chat-mvp1/custom/auth.py /usr/local/lib/python3.5/dist-packages/jupyterhub/

#copy refs to /home
cp -R /root/chat-mvp1/custom/refs/ /home/
mkdir /home/chatscripts
chmod 777 -R /home/chatscripts
