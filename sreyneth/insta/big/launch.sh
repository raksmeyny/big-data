#!/bin/bash
echo "Start user_profile Top post" 

        ./run.sh "annanemati"

echo "Finished user profile"

echo "Start user_profile_detail after with top post"

cat link_userprofile.csv | while read line
do
        python user_profile_detail.py $line
 wait
done
echo "successful user_profile_detail" 

# echo "Start with user comment"
# cat username_com.csv | while read line
# do
#         python ucomment.py $line
#  wait
# done
# echo "successful with user comment" 