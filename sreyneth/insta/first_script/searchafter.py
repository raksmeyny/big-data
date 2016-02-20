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
import datetime
import re
import traceback
import utils
import json
from selenium.webdriver.support.ui import Select
reload(sys)
sys.setdefaultencoding("UTF8")
browser=webdriver.Firefox()

def getElementAttr(selector,attr,parent):
	try:
		elt=parent.find_element_by_css_selector(selector).get_attribute(attr)
		return elt
	except NoSuchElementException,e:
		print "element not found: "+selector
		return "-1"

def getSearchAfter(url):
	browser.get(url)
	gettime=time.strftime("%Y-%m-%d %H:%M:%S")
	try:
		# url='https://instagram.com/explore/tags/'+url
		# browser.get(url)
		try:
			user_name=browser.find_element_by_css_selector('div._8mm5v > h1').get_attribute('textContent')
			print user_name
		except NoSuchElementException:
			user_name = ""
		try:
			post_nb = browser.find_element_by_css_selector('li:nth-child(1) > span > span._e8fkl').get_attribute('textContent')
			print "Post number: " +post_nb
		except NoSuchElementException:
			post_nb = ""
		try:
			following_nb = browser.find_element_by_css_selector('li:nth-child(3) > span > span._bgvpv').get_attribute('textContent')
			print "following number: " +following_nb
		except NoSuchElementException:
			following_nb = ""
		try:
			follower_nb = browser.find_element_by_css_selector('li:nth-child(2) > span > span._pr3wx').get_attribute('textContent')
			print "follower number: " +follower_nb
		except NoSuchElementException:
			follower_nb = ""
		try:
			profile_text = browser.find_element_by_css_selector('div._de9bg > div._bugdy').get_attribute('textContent')
			print profile_text
		except NoSuchElementException:
			profile_text = ""
		try:
			getpost_username=browser.find_elements_by_css_selector(" div > div._nljxa > div> a")
			print len(getpost_username)
			for i in getpost_username:
				getlink=i.get_attribute("href")
				print getlink
				searchlinkafter = io.open('last_link.csv', 'a', encoding='utf8')
				searchlinkafter.write(getlink+"\n")
				#fs.write(getlink+"\n"+username+"\n"+profile_text+"\n"+follower_nb+"\n"+following_nb+"\n")
		except NoSuchElementException:
			print "don't have post"

	except NoSuchElementException:
		print "test"
	
	obj = {
		"username":user_name,
		"profile_text":profile_text,
		"post_nb":post_nb,
		"following_nb":following_nb,
		"follower_nb":follower_nb
		}
	
	myStr=json.dumps(obj)
	nameFile="searchafter_data.json"
	fs = open(nameFile, 'a')
	fs.write(myStr+"\n")

url=sys.argv[1]
getSearchAfter(url)

browser.quit()