
This script will track a list of user on instargram during one week and collect their profile every hour.

I- REQUIREMENTS

Install selenium and python2.7

II- DESCRIPTION

	- user_profile.py: this script will collect the small profile from Instagram users in username.csv and create three files for the ouput
	- ucomment.py: this script will collect the small profile from Instagram commenters from the some user profile in  different json file.
	- launch.sh: this script will call user_profile.py and ucomment.py.
	- runtime.sh: this script will make the script sleep for one 1 hour and relaunch it again.
	- limittime.sh: it will call runtime.sh

III- INPUT

	- username.csv: list of user profile we need to track. (We track their commenters)
	- Some json files: with the username of the commenters

IV-OUTPUT

A folder for each of the profile we tracked, with a json file of the commenters activity inside each of them.

V- HOW TO RUN IT

1. Open terminal and go to your directory.
2. Launch the script ./limittime.sh

