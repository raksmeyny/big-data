#!/bin/bash
echo "Start user_profile Top post"
cat topUser.csv | while read line
do 
         python user_profile.py  $line
 wait
done
echo

echo "Start user_profile_detail after with top post"
cat link_userprofile.csv | while read line
do
        python user_profile_detail.py $line
 wait
done
echo "successful user_profile_detail after 10 min" 
rm -r link_userprofile.csv
