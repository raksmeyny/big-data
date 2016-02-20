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
import re
from selenium.webdriver.support.ui import Select
import urllib
import json
import traceback
from time import gmtime, strftime
import csv
reload(sys)
sys.setdefaultencoding("UTF8")
profile_url=' '

browser = webdriver.Firefox()

def getUserProfileDetail(url):
	browser.get(url)
	#fs = io.open('getlike.csv', 'a', encoding='utf8')
	gettime=time.strftime("%Y-%m-%d %H:%M:%S")
	try:
		username = browser.find_element_by_css_selector('div > a._4zhc5._ook48').get_attribute('textContent')
		print username
	except NoSuchElementException:
		username = ""
	try:
		getdate=browser.find_element_by_css_selector(" section._54eek._56o5u > a > time").get_attribute("title")
		print gettime
	except NoSuchElementException:
		getdate = ""
	try:
		gettitle=browser.find_element_by_css_selector("div > article > div._es1du._rgrbt > ul > li:nth-child(1) > h1").get_attribute("textContent")
		print gettitle
	except NoSuchElementException:
		gettitle = ""
	try:
		like_nb=browser.find_element_by_css_selector("section._54eek._56o5u > div").get_attribute("textContent")
		print like_nb
	except NoSuchElementException:
		like_nb = ""
	# try:
	# 	comment=browser.find_element_by_css_selector('div._es1du._rgrbt > ul > li:nth-child(2)')
	# 	#print comment
	# 	for a in range(0,19):
	# 		comment.click()
			
	# except NoSuchElementException:
	# 	comment = ""
	# try:
	# 	ucom_link=browser.find_elements_by_css_selector('div._es1du._rgrbt > ul > li > a')
	# 	for g in ucom_link:
	# 		getlinkucomment=g.get_attribute('href')
	# 		link = io.open('username_com.csv', 'a', encoding='utf8')
	# 		link.write(getlinkucomment+"\n")
	# 		print getlinkucomment
	# except NoSuchElementException:
	# 	print "link not found"
	try:
		getamoutcomment=browser.find_elements_by_css_selector("ul li._nk46a:not(:first-child)")
		allcomment=len(getamoutcomment)
		number=type(allcomment)
		chanum=str(allcomment)
		value = {
		
		"getcommenttext":[]
		}
		if allcomment >10:

			for l in getamoutcomment[:-10]:
				getcommenttext=l.get_attribute("textContent")
				value["getcommenttext"].append(getcommenttext)
		else:
			for l in getamoutcomment:
				getcommenttext=l.get_attribute("textContent")
				print getcommenttext
				value["getcommenttext"].append(getcommenttext)
	except NoSuchElementException:
		print "not found comment"

	
	obj = {
	
	"username_detail":username,
	"datetime":getdate,
	"title":gettitle,
	"like_nb":like_nb,
	"detail_url":url,
	"all_comment":value["getcommenttext"]
	}
	
	myStr=json.dumps(obj)
	fs = open("post_detail.json", 'a')
	fs.write(myStr+","+"\n")

try:
	url=sys.argv[1]
	getUserProfileDetail(url)
	browser.quit()
except:
	print "Error script "
	traceback.print_exc()
	browser.quit()
