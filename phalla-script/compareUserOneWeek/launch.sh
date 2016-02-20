#!/bin/bash
echo "Start user_profile Top post"
	python user_profile.py
echo "successful user_profile after 10 min" 

echo "Start get user comment"
	python ucomment.py
echo "finish username comment"

# rm -r link_userprofile.csv

#timeout 15s command