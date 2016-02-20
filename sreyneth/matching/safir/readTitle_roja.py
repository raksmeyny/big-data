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
from selenium.webdriver.support.ui import Select
import urllib

reload(sys)
sys.setdefaultencoding("UTF8")
browser=webdriver.Firefox()

def searching(username):
	browser.get("http://www.instagram.com/"+username)
	browser.wait = WebDriverWait(browser, 40)

	try:
		username=browser.find_element_by_css_selector('div._8mm5v > h1').get_attribute('textContent')
		print username
		time.sleep(0.5)
	except NoSuchElementException:
		username = "none"
		username = ""
	try:
		post_nb = browser.find_element_by_css_selector('li:nth-child(1) > span > span._e8fkl').get_attribute('textContent')
		print "Post number: " +post_nb
		time.sleep(0.5)
	except NoSuchElementException:
		post_nb = ""
	try:
		following_nb = browser.find_element_by_css_selector('li:nth-child(3) > span > span._bgvpv').get_attribute('textContent')
		print "following number: " +following_nb
		time.sleep(0.5)
	except NoSuchElementException:
		following_nb = ""
	try:
		follower_nb = browser.find_element_by_css_selector('li:nth-child(2) > span > span._pr3wx').get_attribute('textContent')
		print "follower number: " +follower_nb
		time.sleep(0.5)
	except NoSuchElementException:
		follower_nb = ""
	try:
		profile_text = browser.find_element_by_css_selector('div._de9bg > div._bugdy').get_attribute('textContent')
		print profile_text
		time.sleep(0.5)
	except NoSuchElementException:
		profile_text = ""

	obj = {
		"username":username,
		"profile_text":profile_text,
		"post_nb":post_nb,
		"following_nb":following_nb,
		"follower_nb":follower_nb
		}
	
	myStr=json.dumps(obj)
	nameFile="userroja.json"
	fs = open(nameFile, 'a')
	fs.write(myStr + ",")

with open('rojashop.json') as data_file:    
    data = json.load(data_file)

for line in data:
    #print line["safirstores"]
    username = line["rojashop"]
    try:
    	searching(username)
    except:
    	print "search not match!"
