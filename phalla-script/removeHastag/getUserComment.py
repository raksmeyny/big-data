import subprocess
import json
import re
import os
from collections import Counter

PYTHONIOENCODING="utf-8"

with open('test.json') as data_file:    
    data = json.load(data_file)

for post in data:
	postcomment=post['comment'];
	for i in postcomment:
		tmp3 = re.split("(@[\s\w.]+)",i)
		for a in tmp3:
			tmp2 = a.replace("(@[\s\w.]+)","")
		print tmp2	

		# myStr=json.dumps(tmp2)
		# mystr = myStr+',\n'

		fs = open("RojashopComment.txt", 'a')
		fs.write(tmp2.encode('utf8'))
		# fs.write(mystr)

	
