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

def getSearch(key):
	fs = io.open('link.csv', 'a', encoding='utf8')
	gettime=time.strftime("%Y-%m-%d %H:%M:%S")
	try:
		url='https://instagram.com/explore/tags/'+key
		#url='https://instagram.com/'+key
		browser.get(url)
		
		try:
			allpost=browser.find_element_by_css_selector('article > header > span').get_attribute('textContent')
			print allpost
		except NoSuchElementException:
			print "0"
		try:
			getpost=browser.find_elements_by_css_selector(" div > div._nljxa > div> a")
			print len(getpost)
			for i in getpost:
				getlink=i.get_attribute("href")
				print getlink
				fs.write(getlink+"\n")
		except NoSuchElementException:
			print "don't have post"
		
	except NoSuchElementException:
		print "test"

key=sys.argv[1]
getSearch(key)

browser.quit()