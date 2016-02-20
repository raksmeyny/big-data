#!/bin/bash
	echo '[' >> safirstores.json
	echo '[' >> annanemati.json
	echo '[' >> rojashop.json

timeout -s 9 604800 /home/ubuntu/Desktop/useroneweek/runtime.sh

	echo ']' >> safirstores.json
	echo ']' >> annanemati.json
	echo ']' >> rojashop.json
#limittime -t 30 'runtime.sh'
