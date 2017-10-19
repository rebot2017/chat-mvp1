#!/bin/bash

if [ $# -ne 2 ]; then
	echo "usage: $0 <script-to-copy> <team-folder>"
	exit 1
fi
echo "copying file" $1 "to" $2
cp $1.ipynb ../../$2/	


