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
