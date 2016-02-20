#!/bin/bash
echo "Start get 100 link post"
# cat username.csv | while read line
# do
        python link_comment.py "safirstores"
#  wait
# done
echo "successful link post" 

echo "Start get all comment from safirstores"
cat safirstores.csv | while read line
do
        python comment.py $line
 wait
done
echo "successful safirstores" 

# echo "Start get all comment from annanemati"
# cat annanemati.csv | while read line
# do
#         python comment.py $line
#  wait
# done
# echo "successful annanemati" 