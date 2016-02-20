#!/bin/bash
echo "Start search with google"
cat newTitle.csv | while read line
do
        python getPau.py ${line// /_}

 wait
done
echo "successful" 

echo "Start get review"
cat link.csv | while read line
do
        python make_review.py $line

 wait
done
echo "successful" 