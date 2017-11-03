#!/bin/sh

apt update
apt install -y python3 
apt install -y python3-pip
apt install -y npm
pip3 install jupyterhub
apt-get install -y npm nodejs-legacy
npm install -g configurable-http-proxy
pip3 install notebook
pip3 install jupyterhub-dummyauthenticator
pip3 install bs4


#copy files to appropriate location
mkdir /home/chatscripts
chown nobody:nogroup /home/chatscripts
chmod 777 -R /home/chatscripts
cp -r /root/chat-mvp1/custom/rebot /usr/local/lib/python3.5/dist-packages/
cp -r /root/chat-mvp1/custom/refs /home/
chmod 777 -R /home/refs
