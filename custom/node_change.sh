#!/bin/sh

cd /root/chat-mvp1/
git pull

cp /root/chat-mvp1/custom/auth.py /usr/local/lib/python3.5/dist-packages/jupyterhub/
cp /root/chat-mvp1/custom/login.html /usr/local/share/jupyter/hub/templates/
cp /root/chat-mvp1/custom/login.less /usr/local/share/jupyter/hub/static/
cp /root/chat-mvp1/custom/maintoolbar.js /usr/local/lib/python3.5/dist-packages/notebook/static/notebook/js/
cp -R /root/chat-mvp1/custom/rebot /usr/local/lib/python3.5/dist-packages/


