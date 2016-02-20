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



def getComment(key):
	browser.get(key)
	#scroll(url)	
	try: 
		allcom=browser.find_element_by_css_selector('article > div._es1du._rgrbt > ul > li:nth-child(2)')
		allcom.click()
		print "Click all comment"
	except NoSuchElementException:
		allcom = ""
	try:
		u={
			"getusercom":[]
		}
		usercomment=browser.find_elements_by_css_selector("ul li:not(:first-child) a._4zhc5")
		for l in usercomment:
			usercom=l.get_attribute("textContent")
			u["getusercom"].append(usercom)
	except NoSuchElementException:
		print "No user comment!"
	try:
		c={
			"commenter":[]
		}
		getcomment = browser.find_elements_by_css_selector("div._es1du._rgrbt > ul > li > span")
		for d in getcomment:
			comment = d.get_attribute("textContent")
			c["commenter"].append(comment)
			
	except NoSuchElementException:
		print "No comment!"

	obj = {
		"link":key,
		"username":u["getusercom"],
		"comment":c["commenter"]
	}
	
	myStr=json.dumps(obj)
	fs = open("comment.json", 'a')
	fs.write(myStr+",\n")


key=sys.argv[1]
getComment(key)
browser.quit()


