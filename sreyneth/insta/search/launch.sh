#!/bin/bash
 		./search.sh "sephora"
echo "Start search link Top post"
cat link.csv | while read line
do
        python search_detail.py $line 
 wait
done
echo "successful extract detial after 10 min" 
echo "Start search after with top post"
cat link_after.csv | while read line
do
        python searchafter.py $line
 wait
done
echo "successful extract detial after 10 min" 

echo "Start search after detial with top post"
cat last_link.csv | while read line
do
        python search_detailafter.py $line
 wait
done
echo "successful extract detial after 10 min" 
