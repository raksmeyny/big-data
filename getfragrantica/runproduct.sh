#!/bin/bash
# echo "Start extract link"
# python 1-getabc.py
# wait
# echo "successful extarct link"

# cat getLink.csv | while read line
# do
#         python 2-getallbrand.py $line
#  wait
# done
# echo "successful extract linkproduct"

# cat getlinkproduct.csv | while read line
# do
#         python 3-getbrandinfor.py $line
#  wait
# done
# echo "successful extract getdesignname"

# cat linktoproduct.csv | while read line
# do
#         python 4-getdetail.py $line
#  wait
# done
# echo "successful extract get all data of product"


cat linktoproduct.csv | while read line
do
        python 5-getproductDetail.py $line
 wait
done
echo "successful extract get all data of product"