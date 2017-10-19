#!/bin/bash
git -C /home/user/chat-mvp1/ fetch --all
git -C /home/user/chat-mvp1/ reset --hard origin/master
git -C /home/user/chat-mvp1/ add /home/user/chat-mvp1/chatscripts/$1_*.py /home/user/chat-mvp1/chatapp/$1/*.ipynb /home/user/chat-mvp1/$1/*.py
git -C /home/user/chat-mvp1/ commit -m "$1 auto-commit"
git -C /home/user/chat-mvp1/ push
