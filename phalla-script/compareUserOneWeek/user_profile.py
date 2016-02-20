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
import os
from selenium.webdriver.support.ui import Select
import urllib
import json
import csv
reload(sys)
sys.setdefaultencoding("UTF8")
profile_url=' '

browser = webdriver.Firefox()


def getUserProfile(user):
		
		browser.get("https://www.instagram.com/"+user)
		browser.wait = WebDriverWait(browser, 30)
		url = (browser.current_url)
		gettime=time.strftime("%Y-%m-%d %H:%M:%S")
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
		
		obj = {
			"username":username,
			"Time":gettime,
			"post_nb":post_nb,
			"following_nb":following_nb,
			"follower_nb":follower_nb
			}
		myStr=json.dumps(obj)
		file_name = user+'.json'
		script_dir = os.path.dirname(os.path.abspath(__file__))
		dest_dir = os.path.join(script_dir,user)
		try:
		    os.makedirs(dest_dir)
		except OSError:
		    pass # already exists
		path = os.path.join(dest_dir, file_name)
		with open(path, 'a') as stream:
		    stream.write(myStr+",\n")

		# myStr=json.dumps(obj)
		# nameFile=user+"/"+user+".json"
		# fs = open(nameFile, 'a')
		# fs.write(myStr+",\n")
with open('username.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        user = row[0]
        getUserProfile(user)
browser.quit()
