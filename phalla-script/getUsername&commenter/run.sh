#!/bin/bash
echo "Start get 100 link post"
        python link_comment.py "safirstores"
echo "successful link post" 

echo "Start get all comment from safirstores"
cat safirstores.csv | while read line
do
        python comment.py $line
 wait
done
echo "successful safirstores" 

