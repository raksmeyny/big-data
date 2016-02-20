#!/bin/bash

#add comas and build an array
sed ':a;N;$!ba;s/}\n/},\n/g' allproduct.json > tmp.txt
sed ':a;N;$!ba;s/^{/[{/g' tmp.txt > tmp2.txt
sed ':a;N;$!ba;s/}$/}]/g' tmp2.txt > tmp3.txt

#remove the temporary files
mv tmp3.txt allproductcleaned.json
rm tmp*.txt
