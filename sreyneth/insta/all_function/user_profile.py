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
import traceback
reload(sys)
sys.setdefaultencoding("UTF8")
profile_url=' '
date = ""
avg=""
username=''
browser = webdriver.Firefox()

def getUserProfile(key):
		url="https://www.instagram.com/"+key
		browser.get(url)
		browser.wait = WebDriverWait(browser, 30)
		
		try:
			username=browser.find_element_by_css_selector('div._8mm5v > h1').get_attribute('textContent')
			print username
		except NoSuchElementException:
			username = ""
		try:
			fname=browser.find_element_by_css_selector('div._de9bg > div._bugdy > h2').get_attribute('textContent')
			print fname
		except NoSuchElementException:
			fname = ""
		try:
			profile_pic= browser.find_element_by_css_selector('div._o0ohn > img').get_attribute('src')
			print profile_pic
		except NoSuchElementException:
			profile_pic = ""
		try:
			website= browser.find_element_by_css_selector('div._de9bg > div._bugdy > a').get_attribute('href')
			print website
		except NoSuchElementException:
			website = "Private Account"
		try:
			post_nb = browser.find_element_by_css_selector('li:nth-child(1) > span > span._e8fkl').get_attribute('textContent')
			print "Post number: " +post_nb
		except NoSuchElementException:
			post_nb = "Private Account"
		try:
			following_nb = browser.find_element_by_css_selector('li:nth-child(3) > span > span._bgvpv').get_attribute('textContent')
			print "following number: " +following_nb
		except NoSuchElementException:
			following_nb = "Private Account"
		try:
			follower_nb = browser.find_element_by_css_selector('li:nth-child(2) > span > span._pr3wx').get_attribute('textContent')
			print "follower number: " +follower_nb
		except NoSuchElementException:
			follower_nb = "Private Account"
		try:
			profile_text = browser.find_element_by_css_selector('div._de9bg > div._bugdy').get_attribute('textContent')
			print profile_text
		except NoSuchElementException:
			profile_text = "Private Account"
		try:
			getpost=browser.find_elements_by_css_selector(" div > div._nljxa > div> a")
			print len(getpost)
			
			for i in getpost:
				getlink=i.get_attribute("href")
				print getlink
				link = io.open('link_userprofile.csv', 'a', encoding='utf8')
				link.write(getlink+"\n")
				
		except NoSuchElementException:
			print "don't have post"
		date = ""
		avg = ""
		try:
			link=[]
			arr = []
			a=[]
			sumLike = 0
			allpost=browser.find_elements_by_css_selector('div > div._nljxa > div> a')
			for g in allpost:
				getallpost=g.get_attribute("href")
				link.append(getallpost)
			i=0
			for n in link:
					print "prit i"
					print i
					browser.get(n)
					time.sleep(2)
					try:
						avg_like=browser.find_element_by_css_selector("section._54eek._56o5u > div").get_attribute("textContent")
						like = avg_like.replace("likes","")
						like=like.replace("k","000")
						like=like.strip()
						print like
						like = float(like)
						arr.append(like)
						print arr
						sumLike = sum(arr)
						print sumLike
						avg = sumLike / len(arr)
						print avg

					except NoSuchElementException:
						avg_like = "Private Account"
					if(i==0):
						try:
							date=browser.find_element_by_css_selector('section._54eek._56o5u > a > time').get_attribute('title')
							print date
						except NoSuchElementException:
							date = "Private Account"
					i=i+1
		except NoSuchElementException:
			allpost = ""
		if username == "":
			print "not fount"
		else:
			if date == "" or avg == "":
				obj = {
					"Username":username,
					"Full_name":fname,
					"Website":website,
					"Profile_picture":profile_pic,
					"Bio":profile_text,
					"Number_of_post":post_nb,
					"Number_of_following":following_nb,
					"Number_of_follower":follower_nb,
					"Date_of_last_post":"Private Account",
					"Average_like":"Private Account"
					}
			
				myStr=json.dumps(obj)
				fs = open('user_profile.json', 'a')
				fs.write(myStr+",\n")
			else:
				obj = {
					"Username":username,
					"Full_name":fname,
					"Website":website,
					"Profile_picture":profile_pic,
					"Bio":profile_text,
					"Number_of_post":post_nb,
					"Number_of_following":following_nb,
					"Number_of_follower":follower_nb,
					"Date_of_last_post":date,
					"Average_like":avg
					}
			
				myStr=json.dumps(obj)
				fs = open('user_profile.json', 'a')
				fs.write(myStr+",\n")

				
try:
	key=sys.argv[1]
	getUserProfile(key)
	browser.quit()
except:
	print "Error script "
	traceback.print_exc()
	browser.quit()