#!/bin/bash

sed ':a;N;$!ba;s/}\n/},\n/g' $1 > data2.json
sed ':a;N;$!ba;s/^{/[{/g' data2.json > data3.json
sed ':a;N;$!ba;s/}$/}]/g' data3.json > data4.json
mv data4.json $2
rm -i data*.json

# sed ':a;N;$!ba;s/}\n/},\n/g' $3 > view2.json
# sed ':a;N;$!ba;s/^{/[{/g' view2.json > view3.json
# sed ':a;N;$!ba;s/}$/}]/g' view3.json > view4.json
# mv view4.json $4
# rm -i view*.json
