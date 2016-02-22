This script will get userprofile of users top in safirstores in every 5 minute in 5 hour.
it mean when we finished launch this script it will sleep 5 minute and after 5m it will lauch it again in 5 hour. 
(In 5 hour it will be automatically to stop the script)

I- REQUIREMENTS
	
	Install selenium and python2.7

II- DESCRIPTION

	-readTitle.py: get userprofile of all users.
	-topUser.json: list all top user in safir.
	-launch.sh: to launch the script of readTitle.py
	-run.sh: limit time sleep in 5 minute after the script is finished launch.
	-limittime.sh: set limit time in 5 hour (this script will launch every 5 minute in 5 hour)

III- INPUT

	- topUser.json: list of users top.

IV-OUTPUT

	- usersafir.json: list all the username, following number, follower number, post number and also description.
	
V- HOW TO RUN IT

1. Open terminal and go to your directory.
2. Launch the script ./limittime.sh

