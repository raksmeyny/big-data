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

# fs = open("safir_user_comment.json", 'a')
# fs.write("[\n")


def getprofile(name,a):
	url="https://www.instagram.com/"+name
	browser.get(url)
	browser.wait = WebDriverWait(browser, 30)
	url = (browser.current_url)
	
	try:
		username=browser.find_element_by_css_selector('div._8mm5v > h1').get_attribute('textContent')
		print username
	except NoSuchElementException:
		username = ""
	try:
		post_nb = browser.find_element_by_css_selector('li:nth-child(1) > span > span._e8fkl').get_attribute('textContent')
		print "Post: " +post_nb
	except NoSuchElementException:
		post_nb = ""
	try:
		following_nb = browser.find_element_by_css_selector('li:nth-child(3) > span > span._bgvpv').get_attribute('textContent')
		print "Following: " +following_nb
	except NoSuchElementException:
		following_nb = ""
	try:
		follower_nb = browser.find_element_by_css_selector('li:nth-child(2) > span > span._pr3wx').get_attribute('textContent')
		print "Follower: " +follower_nb
	except NoSuchElementException:
		follower_nb = ""
	try:
		twolast=[]
		twolastpost = browser.find_elements_by_css_selector('div > a._8mlbc')
		count=0
		for tlp in twolastpost:
			if count >= 2:
				break
			else:
				link=tlp.get_attribute("href")
				twolast.append(link)
				count =count +1 
		like1={
			"Nb_like":[]
		}
		com={
			"Nb_comment":[]
		}
		for url in twolast:
			print url
			browser.get(url)
			time.sleep(2)
			try:
				like = browser.find_element_by_css_selector('div._qwn3t span span:nth-child(2)').get_attribute('textContent')
				like1["Nb_like"].append(like)
			except NoSuchElementException:
				like = browser.find_elements_by_css_selector('div._qwn3t a')
				l = len(like)
				like1["Nb_like"].append(l)
			try: 
				comment=browser.find_element_by_css_selector('button._l086v span:nth-child(2)').get_attribute('textContent')
				com["Nb_comment"].append(comment)
			except NoSuchElementException:
				comment=browser.find_elements_by_css_selector("ul > li._nk46a:not(first-child) > a")
				getcomment = len(comment)
				com["Nb_comment"].append(getcomment)
	except NoSuchElementException:
		twolastpost = ''
	
	obj = {
		"Username":username,
		"Post_nb":post_nb,
		"Following_nb":following_nb,
		"Follower_nb":follower_nb,
		"Last two post":{
			"Like":like1["Nb_like"],
			"comment":com["Nb_comment"]
		}	
	}
	if a == "safirstores_user":
		myStr=json.dumps(obj)
		fs = open("safirstores/safirstores.json", 'a')
		fs.write(myStr+",\n")
	elif a == "annanemati_user":
		myStr=json.dumps(obj)
		fs = open("annanemati/annanemati.json", 'a')
		fs.write(myStr+",\n")
	else:
		myStr=json.dumps(obj)
		fs = open("rojashop/rojashop.json", 'a')
		fs.write(myStr+",\n")

arr = ["safirstores_user", "annanemati_user", "rojashop_user"]
counter = 0
for a in arr:
	with open(a+'.json') as data_file:    
	    data = json.load(data_file)
	for d in data:
		user=d['username']
		print user
		for u in user:
		  	getprofile(u,a)

	counter = counter+1	