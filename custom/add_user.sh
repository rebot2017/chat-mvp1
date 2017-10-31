#!/bin/sh

useradd -p `mkpasswd 123` $1
mkdir /home/$1

cp /home/refs/* /home/$1

chown -R $1 /home/$1