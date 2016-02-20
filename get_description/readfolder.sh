#!/bin/bash
echo "Start read folder"
cat done.csv | while read line
do
        python readfolder.py ${line// /_}

 wait
done
echo "successful extract read folder"
