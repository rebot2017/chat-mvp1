#!/bin/bash
echo "team num: " $1
git -C /home/user/chat-mvp1/ add /home/user/chat-mvp1/custom/refs/*
git -C /home/user/chat-mvp1/ commit -m "$1 auto-commit"
git -C /home/user/chat-mvp1/ push -f origin master
