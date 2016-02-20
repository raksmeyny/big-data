#!/bin/bash
# echo "Start get link products"
#          python getlink.py  $line
# echo "Finished get link products"

echo "Start get link products"
cat menu.csv | while read line
do 
         python linkpro.py  $line
 wait
done
echo "Finished get link products"