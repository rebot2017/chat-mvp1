#apt install -y nfs-kernel-server


#mkdir /home/chatscripts
#chown nobody:nogroup /home/chatscripts
#chmod 777 /home/chatscripts



echo '/home/chatscripts 139.59.110.66(rw,no_subtree_check,no_root_squash,sync)' >> /etc/exports
#echo '/home/chatscripts 139.59.110.66(rw,no_subtree_check,no_root_squash,sync)' >> /etc/exports

systemctl restart nfs-kernel-server
