#!/bin/sh


#installing dependencies
apt install python3
apt install pip3
pip3 install jupyterhub
apt install npm nodejs-legacy
npm install -g configurable-http-proxy
pip3 install --upgrade notebook


# adding custom authentication hook
cp auth.py /usr/local/lib/python3.5/dist-packages/jupyterhub/

#copy refs to /home
cp -R refs/ /home/refs/


