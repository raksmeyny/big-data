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

def getUserProfile():
		browser.get("https://www.instagram.com/safirstores/")
		browser.wait = WebDriverWait(browser, 30)
		url = (browser.current_url)
		scroll(url)
		try:
			username=browser.find_element_by_css_selector('div._8mm5v > h1').get_attribute('textContent')
			print username
		except NoSuchElementException:
			username = ""
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
			getpost=browser.find_elements_by_css_selector(" div > div._nljxa > div> a")
			print len(getpost)
			for i in getpost:
				getlink=i.get_attribute("href")
				print getlink
				link = io.open('link_userprofile.csv', 'a', encoding='utf8')
				link.write(getlink+"\n")
		except NoSuchElementException:
			getpost = ""
		
		
		obj = {
			"username":username,
			"profile_text":profile_text,
			"post_nb":post_nb,
			"following_nb":following_nb,
			"follower_nb":follower_nb
			}
		
		myStr=json.dumps(obj)
		nameFile="userprofile.json"
		fs = open(nameFile, 'a')
		fs.write(myStr+"\n")

getUserProfile()
browser.quit()
	
