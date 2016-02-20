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
import csv
reload(sys)
sys.setdefaultencoding("UTF8")
#browser=webdriver.Firefox()
profile_url=' '
browser = webdriver.Firefox()
def scroll(url):
	try:
	    browser.wait = WebDriverWait(browser, 5)
	    browser.get(url)
	    browser.wait = WebDriverWait(browser, 5)
	    box = browser.wait.until(EC.presence_of_element_located((By.ID, "doc")))

	    for i in range(1,10):
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
def getLinkComment(key):
	url='https://instagram.com/'+key
	browser.get(url)
	
	try:
		link=browser.find_element_by_css_selector("article > div > div._pupj3 > a")
		link.click()
		print "success click"
	except NoSuchElementException:
		print "no click"
	try:
		for i in range(7):
			time.sleep(2)
			browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			print "scrolling Now"
			browser.execute_script("window.scrollBy(0, -50);")
			print "scrool back"
			
	except NoSuchElementException:
		print "no scroll"
	try:
		allpost=browser.find_elements_by_css_selector(" div > div._nljxa > div> a")
		print len(allpost)
		for i in allpost:
			getlink=i.get_attribute("href")
			print getlink
			link = io.open('link_comment.csv', 'a', encoding='utf8')
			link.write(getlink+"\n")

	except NoSuchElementException:
		print "not found readmore"


key=sys.argv[1]
getLinkComment(key)
browser.quit()

	