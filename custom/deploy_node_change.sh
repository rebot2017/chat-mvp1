#!/bin/sh

ipaddrfile="/root/chat-mvp1/custom/ipaddress.txt"

while read -r line
do
    echo "$line"
    ssh root@$line -i ~/.ssh/whdigitalocean 'bash -s' < node_change.sh

done < $ipaddrfile
