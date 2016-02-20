#!/bin/bash
while true
do
	echo '[' >> safirstores.json
	echo '[' >> annanemati.json
	echo '[' >> rojashop.json

	/home/ubuntu/Desktop/useroneweek/launch.sh

	echo '{}],' >> safirstores.json
	echo '{}],' >> annanemati.json
	echo '{}],' >> rojashop.json
 sleep 60m
done
