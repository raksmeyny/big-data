This script is search with key name (EX: safirstores)

I- REQUIREMENTS
	
	Install selenium and python2.7

II- DESCRIPTION

	-search.py: get all link in 12 posts of the users.
	-link.csv: store all link in 12 post
	-search_detail.py: get post details of all users.
	-link_after.csv: store all link user profile of user in post detail
	-searchafter.py: get all user profile of all the users.
	-last_link.csv: store all link post details of username that get from search_detail.py.
	-search_detail_after.py: get post details of each users.
	-launch.sh: this file is for launch all the script above with key name.

III- INPUT


IV-OUTPUT

	-search_data.json: store data of post detail (EX: comment, like, date...).
	-searchafter_data.json: store all data of user profile (username get from search_detail.py), and also post details.

	
V- HOW TO RUN IT

1. Open terminal and go to your directory.
2. Launch the script ./launch.sh

