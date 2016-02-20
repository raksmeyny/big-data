#!/bin/bash
# echo "Start user_profile Top post"
#         python user_profile.py $line
# echo "successful user_profile after 10 min" 

# echo "Start user_profile_detail after with top post"
cat link_userprofile.csv | while read line
do
        python user_profile_detail.py $line
 wait
done
echo "successful user_profile_detail after 10 min" 

# echo "Start search with keyword"
#  		./search.sh "mariamrod"

# echo "Start  get detail top post"

# cat link.csv | while read line
# do
#         python search_detail.py $line 
#  wait
# done
# echo "successful extract detial after 10 min" 

# echo "Start search after with top post"
# cat link_after.csv | while read line
# do
#         python searchafter.py $line
#  wait
# done
# echo "successful extract detial after 10 min" 

# echo "Start search after detial with top post"
# cat last_link.csv | while read line
# do
#         python search_detailafter.py $line
#  wait
# done
# echo "successful extract detial after 10 min" 
