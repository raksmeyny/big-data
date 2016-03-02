#!/usr/bin/python

import pandas
import json


def searchIndex(l,values):
	index=-1
	val = values
	for i in range(len(l)):
		if l[i] == values:
			index = i
	return val,index

def returnMatch(list1,list2):
	''' for each item in list1 returnMatch will return a list of tuple made of all the element of list1
	found in list2, and the corresponding index
	'''
	matched=[]
	for i in range(len(list1)):
		value=list1[i]
		matchedvalue=searchIndex(list2,value)
		matched.append(matchedvalue)

	return matched

def buildDict(list1,list2):
	dictionary = {}
	for i in range(len(list1)):
	    dictionary[list1[i]] = list2[i]
	
	# print dictionary

	myStr=json.dumps(dictionary)
	mystr=myStr+',\n'
		
	fs = open("barcode_match.json", 'a+')
	fs.write(mystr) 
	 
	return dictionary

l = [1,5,3,2,6,5,4]
# list1=[7,6,3,8,0]
# list2=[5,1,2,3,1]

df = pandas.read_csv("sales_matched_old.csv",usecols=['Barcode','product_name'])

list1 = list(df["Barcode"])
list2 = list(df["product_name"])


index,value=searchIndex(l,4)
print 25,buildDict(list1,list2)

