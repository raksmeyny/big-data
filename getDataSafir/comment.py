import time
from datetime import datetime
from time import mktime
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
import csv
reload(sys)
sys.setdefaultencoding("UTF8")
profile_url=' '
browser = webdriver.Firefox()

def scroll(url):
	try:
	    browser.wait = WebDriverWait(browser, 5)
	    browser.get(url)
	    browser.wait = WebDriverWait(browser, 5)
	    box = browser.wait.until(EC.presence_of_element_located((By.ID, "doc")))

	    for i in range(1,2):
	    	print "scrolling"
	    	browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	    	time.sleep(2)
	    print 'scrolling finish'
	    return 1
	except NoSuchElementException,e:
		print 'Error in scrolling of '+url+' :'
		print(traceback.format_exc())
	except TimeoutException,e:
		print 'Sroll: Time out for '+url+' :'

def getComment(key):
	url = browser.get(key)
	#scroll(url)	

	try:
		like = browser.find_element_by_css_selector('div > span > span:nth-child(2)').get_attribute('textContent')
		print like
	except NoSuchElementException:
		like = ''

	try:
		dates = browser.find_element_by_css_selector('a > time').get_attribute('datetime')
		date2 = dates.replace('T'," ").replace('.000Z',"")
		date1 = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")
		date =mktime(date1.timetuple())
		print date
	except NoSuchElementException:
		date = ''

	try: 
		amoutcome=browser.find_element_by_css_selector('ul > li:nth-child(2) > button > span:nth-child(2)').get_attribute('textContent')
		amoutcoment=int(amoutcome)
		print amoutcoment
		obj = {
		"link":key,
		"date":date,
		"likes":like,
		"comment":amoutcoment
		}
		print obj
		myStr=json.dumps(obj)
		nameFile="comment.json"
		fs = open(nameFile, 'a')
		fs.write(myStr+",\n")
	except NoSuchElementException:
		getamoutcomment=browser.find_elements_by_css_selector("ul li._nk46a:not(:first-child)")
		getamountcom = len(getamoutcomment)
		print getamountcom
		obj = {
		"link":key,
		"date":date,
		"likes":like,
		"comment":getamountcom
		}
		print obj
		myStr=json.dumps(obj)
		nameFile="comment.json"
		fs = open(nameFile, 'a')
		fs.write(myStr+",\n")

key=sys.argv[1]
getComment(key)
browser.quit()

	