#!/bin/bash
echo "Start extract link menu"
cat name.csv | while read line
do
    python getblog.py ${line// /+}
 wait
done
echo "successful extract linkproduct"
