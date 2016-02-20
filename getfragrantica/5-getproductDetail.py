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
def getAccordname(url):
	browser.wait = WebDriverWait(browser, 50)
	try:
		getAccords=browser.find_elements_by_css_selector("#prettyPhotoGallery > div:nth-child(1) > div:nth-child(n) > span")
		getRang=browser.find_elements_by_css_selector("#prettyPhotoGallery > div:nth-child(1) > div:nth-child(n) > div")
		print len(getRang)
		for s in getRang:
			getWidth = s.get_attribute("style")
			print getWidth
		values = {
			"accords":[]
		}
		# for l in getRang:
		# 	getWidth = l.get_attribute("")
		i = 0
		for l in getAccords:
			getText=l.get_attribute("textContent")
			# getStyle= getRang[i].get_attribute("style")

			# soup = BeautifulSoup(getStyle,'html.parser') 
			# my_att = [i.attrs['style'] for  i in soup.find_all("div")]
			# css = ''.join(my_att)
			# print css
			# width_list = map(float,re.findall(r'(?<=width:)(\d+)(?=px;)', css))
			# print np.mean(width_list) 
			# print getStyle
			# getStyle= re.sub("/width. \d+\w.;/g",getStyle)
			# print getStyle
			obj ={
				"title": getText,
				# "rang": getStyle		
			}
			i = i +1
			# print obj
			values["accords"].append(obj)
		# print values;
		return values
	except NoSuchElementException:
		print "Not found accords"
def getrate():
	try:
		getrate=browser.find_elements_by_css_selector('#resultsWrapper > div > div:nth-child(2) > input[type="radio"]:nth-child(n)')
		# print len(getrate)
		
		for i in getrate:
			i.click()
			time.sleep(2)
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
				# print values

			except NoSuchElementException:
				print "not found"
				return -1
	except NoSuchElementException:
		print "not click"
	
try:
	url=sys.argv[1]
	browser.get(url)
	getaccordname=getAccordname(url)
	getrate=getrate()
	# finalObject = {
	# 	"getAccordname":getaccordname["accords"],
	# 	"getrate": getrate["ratings"]
	# }
	# print finalObject
	# myStr=json.dumps(finalObject)
	# # print myStr
	# nameFile="myallproduct.json"
	# fs = open(nameFile, 'a')
	# fs.write(myStr+"\n")
	browser.quit() 
except:
	print "Error script "
	browser.quit()
