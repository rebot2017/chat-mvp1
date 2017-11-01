#!/bin/sh
echo "$#"
if [ $# !=  1 ]; then
	echo "add IP address of master as arg1"
	exit 1
fi

#ping master to get master to allow our ipaddress to connect to NFS
ipaddr=`hostname -I | awk '{print$1}'`
curl "http://$1:5000/ipaddr/$ipaddr"
echo $ipaddr
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
cp /root/chat-mvp1/custom/login.html /usr/local/share/jupyter/hub/templates/
#copy refs to /home
cp -R /root/chat-mvp1/custom/refs/ /home/

#mount chatscript from host server instead
mkdir /home/chatscripts
chmod 777 -R /home/chatscripts

#setting up NFS on client
apt install -y nfs-common


mount $1:/home/chatscripts /home/chatscripts
chmod 777 -R /home/chatscripts
