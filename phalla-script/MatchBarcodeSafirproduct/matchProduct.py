import json
import csv

PYTHONIOENCODING='utf-8'

with open("products.json") as json_file:
    json_data = json.load(json_file)

with open('all_product_to_collect.csv') as csvfile:
	read_csv = csv.DictReader(csvfile)


	for row in read_csv:
		item = row['ItemName']
		barcode = row['Barcode']
		csvfile = (row['Barcode'], row['ItemName'])

		for j in json_data:
			if (item==j['title'] ) or (j['title']==item ):
				j['Safir_name']=item
				j['Barcode']=barcode
			else:
				j['Safir_name']=''
				j['Barcode']=0

	myStr=json.dumps(json_data)
	mystr = myStr+"\n"
	fs = open("newProducts.json", 'a')
	fs.write(mystr)

	# 	for each in read_csv:
	#   		data = {}
	# 	  	for field in csvfile:
	# 	  		data[field] = field[1]
	# 	  	print data

	# for post in range(len(json_data)):
	# 	value = json_data[post]
	# 	postTitle = value["title"]
		# print json_data[post]['title'][5]
	




# csvfile = open("test.csv", 'r')
# jsonfile = open("test.json", 'w')

# reader = csv.DictReader(csvfile)
# for row in reader:
# 	fieldnames = (row['Barcode'], row['ItemName'])
# print fieldnames
# output = []

# for each in reader:
#   row = {}
#   for field in fieldnames:
#     row[field] = each[field]
# output.append(row)
# print output

# json.dump(output, jsonfile, indent=2, sort_keys=True)



	