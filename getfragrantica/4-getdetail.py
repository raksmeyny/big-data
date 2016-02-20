import time
import io
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium import selenium
import selenium 
import json
import re
from selenium.webdriver.support.ui import Select
import urllib
import csv
reload(sys)
sys.setdefaultencoding("UTF8")
browser = webdriver.Firefox()
#browser=webdriver.PhantomJS()
def getProductband(url):
	
	linkproduct=url.rsplit("/",1)[-1]
	curl=linkproduct.rsplit("-",-1)[-1]
	cuturl=curl.replace(".html","")
	
	browser.wait = WebDriverWait(browser, 50)
	#script for got title of product
	
	try:
		titlepro=browser.find_element_by_css_selector("#col1 > div > div > h1").get_attribute("textContent")
		print titlepro
		values={
			"brand": []
		}
		
		obj={
				"_id":cuturl,
			 	"name":titlepro	
  	 		}
  	 	print "MY BRANDLIST"
  	 	values["brand"].append(obj)
 	 	# return values
 	 	return values
	except NoSuchElementException:
		print "title not found"
		return -1
def getbrandcategory():

	try:
		getbrandname=browser.find_element_by_css_selector("#col1 > div > div > p > span:nth-child(1)").get_attribute("textContent")
		
		values={
			"category":[]
		}
			
		cutgetbrandname = getbrandname.replace("Designers","")
		obj={
			 	"brand":cutgetbrandname	
  	 		}
  	 	values["category"].append(obj)
	 	
		return values

	except NoSuchElementException:
		print "band not found"
		return -1

	
def getCommment():
	try:
		allComment=browser.find_elements_by_css_selector("div.pwq")
		values={
			"comments":[]
		}
		i=0
		for l in allComment:
			try:
				username=l.find_element_by_css_selector("div.avatar a b").get_attribute("textContent")
			except NoSuchElementException:
				print "username not found"
			try:
				comments=l.find_element_by_css_selector("div.revND p").get_attribute("textContent")
			except NoSuchElementException:
				print "comments not found"
			try:
				dateusecommend=l.find_element_by_css_selector("div.dateND").get_attribute("textContent")
			except NoSuchElementException:
				print "dateusecommend not found"
			if not username:
				print "no username , file not write"

			else:
				obj={
				 	"user":username,
		 	 		"text":comments,
		 	 		"dateusecommend":dateusecommend
	 	 		}
	 	 		values["comments"].append(obj)
		return values
	except NoSuchElementException:
		print "comments not found"
		return -1

def mainaccords():

	
	browser.wait = WebDriverWait(browser, 50)
	try:
		get_scent=browser.find_element_by_css_selector("#prettyPhotoGallery > div:nth-child(1)")
		mystyle="width: 130px; height: 20px; border-right: 1px solid rgb(255, 255, 255); border-width: medium 1px 1px; border-style: none solid solid; border-color: -moz-use-text-color rgb(255, 255, 255) rgb(255, 255, 255); -moz-border-top-colors: none; -moz-border-right-colors: none; -moz-border-bottom-colors: none; -moz-border-left-colors: none; border-image: none; position: relative; text-align: center; clear: both; padding: 0px;"

		category=get_scent.find_elements_by_tag_name("div")
		values={
			"accords":[]

		}
		for l in category:
			getstyle=l.get_attribute("style")
			if getstyle == mystyle:
				rate=l.find_element_by_tag_name("div").get_attribute("style")
				rate=re.sub(r"\s+",'',rate)
				rate=re.match("(width:\d+px)",rate)
				if rate:
					rate= rate.group(1)
					rate=re.sub(r"[^\d+]",'',rate)
					print rate
					title=l.find_element_by_tag_name("span").get_attribute("textContent")
					print title
					obj={
						"title":title,
						"rate":rate
					}
					values["accords"].append(obj)
			else:
				print "title not found"
		return values
	except NoSuchElementException:
	 	print "image not found"
		return -1

def perfume_Pyramid():
	
	
	
	browser.wait = WebDriverWait(browser, 50)
	try:
		perfumePyramid=browser.find_elements_by_css_selector('#col1 > div > div > div:nth-child(9) > div:nth-child(1) p')
		
		values={
			'pyramid':[]
		}
		i=0
		for l in perfumePyramid:
			try:
				categorytitle =l.find_element_by_tag_name("b").get_attribute("textContent")
			except NoSuchElementException:
				print "categorytitle not found"
				categorytitle=''
			try:

				Perfume_Pyramid=l.find_elements_by_css_selector("span img")
			except NoSuchElementException:
				categorytitle=''
				print ""
			for i in Perfume_Pyramid:
				titleimg=i.get_attribute("bt-xtitle")
				print "title="+titleimg
				if categorytitle=='':
					obj={
						   "title":titleimg
					}
					values["pyramid"].append(obj)
				else:
					obj={
						categorytitle:{
						   "title":titleimg
						}
					}
					values["pyramid"].append(obj)
					print "Perfume_Pyramid"
					print values

		return values		
		
	except NoSuchElementException:
		print "Perfume_Pyramid not found"
		return -1
	

def main_note():
	
	browser.wait = WebDriverWait(browser, 50)
	try:
		mainNotes=browser.find_elements_by_css_selector("div#userMainNotes div")
		
		values = {
			"note":[]
		}
		i =0
		for b in mainNotes:
			try:
				title=b.find_element_by_tag_name("img").get_attribute("alt")
			except NoSuchElementException:
				print "title not found"
			try:
				nb_vote=b.find_element_by_css_selector("span").get_attribute("textContent")
			except NoSuchElementException:
				print "nb_vote not found"
			obj={
	   			 	"title":title,
	   			 	"numbervote":nb_vote	
	     	 		}
	     	 	values["note"].append(obj)
  	 	 	
		return values
	except NoSuchElementException:
		print "resultvote not found"
		return -1
	
def user_rating():
	
	try:
		diagramresult=browser.find_elements_by_css_selector("div#diagramresult div")
 		
		
		feeling =browser.find_elements_by_css_selector(".votecaption")
		

		values={
			"ratings":[]
		}
		i=0
		
		for l in diagramresult:
			
			currentHeight=l.size
			currentFeel=feeling[i].get_attribute("textContent")
			obj={
				"feel":currentFeel,
				"value":currentHeight["height"]
			}
			
			values["ratings"].append(obj)
			i=i+1
		return values
			
	except NoSuchElementException:
		print "not found"
		return -1



def total_people_vote():

	
	
	browser.wait = WebDriverWait(browser, 50)
	try:
		
		poeplevote =browser.find_element_by_css_selector("#resultsWrapper > div > div:nth-child(1) b").get_attribute("textContent")
		poeplevotedict = {}

		values={
			"vote":[]
		}
		obj={
			"Total people voted":poeplevote
			
		}
		values["vote"].append(obj)
		return values
			
	except NoSuchElementException:
		print "not found"
		return -1

def getlikeofproduct():
	browser.wait = WebDriverWait(browser, 50)
	try:
		getlikeofproduct=browser.find_elements_by_css_selector("div.fl")
		values={
			"amoutlikes":[]
		}
		for l in getlikeofproduct:
			try:
				getproductname=l.find_element_by_css_selector("img").get_attribute("alt")
			except NoSuchElementException:
				print "getproductname not found"
			try:
				getamoutlike=l.find_element_by_css_selector("span.fsi").get_attribute("textContent")
			except NoSuchElementException:
				print "getamoutlike not found"
			if getproductname =="" and getamoutlike=="":
				print "no getamoutlike and getproductname"
				return
			else:
				obj={
					"productname":getproductname,
					"amoutlike":getamoutlike
				}

				values["amoutlikes"].append(obj)
		return values
	except NoSuchElementException:
		print "getlikeofproduct not found"
def getpeopleihave():
	try:
		getpeopleihave=browser.find_element_by_css_selector("#mainpicbox > p > span").get_attribute("textContent")
		ihave=re.sub(r"\s+",'',getpeopleihave)
		ihave=re.sub(r"[^\d+]",',',ihave)
		ihave=re.sub(r"\,+",',',ihave)
		ihave=ihave[1:]
		ihave=ihave.split(",",4)
		print type(ihave)
		text=["I have it","I had it","I want it","My signature"]
		values={
			"ihave":[]
		}
		i=0
		for l in ihave:
			texts=text[i]
			print texts
			obj={
				texts:l
			}
			values["ihave"].append(obj)	
			i = i + 1	
		print values
		return values
	except NoSuchElementException:
		print "getpeopleihave can not found"
def cleanAccord(accords):
	print "abc"
	print accords
	final={
		"accords":[]
	}
	for a in accords:
		print "ACCORD"
		print json.dumps(a)
		if a.has_key('mainaccords'):
			final["accords"].append(a["mainaccords"])
	return final

def getId(url):
	curId=url.split('/')[-1]
	curId=curId.split('-')[-1]
	curId=curId.split('.')[-2]
	return curId




try:
	url=sys.argv[1]
	browser.get(url)
	brandid=getProductband(url)
	#print(json.dumps(brandid))
	brandcategory=getbrandcategory()
	comments=getCommment()
	accords=mainaccords()
	pyramid=perfume_Pyramid()
	mainNote=main_note()
	amoutlikes=getlikeofproduct()
	rate=user_rating()
	totalvote=total_people_vote()
	getpeopleihave=getpeopleihave()
	finalAccord=mainaccords()
	idProduct=getId(url)
	finalObject={
		"id_product":idProduct,
		"product_name":brandid["brand"][0]['name'],
		"brand_name":brandcategory,
		"comments":comments["comments"],
		"accords":accords["accords"],
		"pyramid":pyramid,
		"rate":rate,
		"amout_likes":amoutlikes["amoutlikes"],
		"peoplevote":getpeopleihave["ihave"],
		"mainNote":mainNote,
		"totalvote":totalvote
	}
	print "MY FINAL OBJECTTT DJIB"
	myStr=json.dumps(finalObject)
	print myStr
	nameFile="allproduct.json"
	fs = open(nameFile, 'w')
	fs.write(myStr+"\n")
	browser.quit() 
except:
	print "Error script "
	browser.quit()
