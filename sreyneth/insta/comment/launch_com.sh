#!/bin/bash
echo "Start get 100 link post"
        python link_comment.py $line "rojashop"
echo "successful link post" 

echo "Start get all comment post"
cat link_comment.csv | while read line
do
        python comment.py $line
 wait
done
echo "successful get comment" 