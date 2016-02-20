import json

# with open('newTitle.json') as f:
#     # load json objects to dictionaries
#     jsons = map(json.loads, f)

# uniques = {x['title']: x for x in jsons}

# # write to new json file
# with open('data.json' ,'w') as nf:
#     json.dump(uniques.values(), nf)

# print uniques.values()


file=open("newTitle.json")
json_data=json.load(file)
print len(json_data)

json_data_noDuplicate={j['title'] for j in json_data}
print len(json_data_noDuplicate)
# fs = open("data.json", 'a')
# fs.write()
#json_data_noDuplicate

#print sorted(json_data_noDuplicate)

# uniqlines = set(open('newTitle.json').readlines())
# bar = open('newTitle.json', 'w').writelines(set(uniqlines))
