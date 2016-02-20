import csv
import json

with open('comment.json') as x:    
   	x = json.load(x)
   	print x
with open('data.csv','a') as f:    
	csvfile=csv.writer(f)
	for item in x:
		csvfile.writerow([item["date"],item["comment"],item["link"],item["likes"]]);
# f = csv.writer(open("comment.csv", "w+"))

# f.writerow(["date", "comment", "link", "likes"])

# for x in x:
#     f.writerow([x["date"], 
#                 x["comment"], 
#                 x["link"], 
#                 x["likes"]])
