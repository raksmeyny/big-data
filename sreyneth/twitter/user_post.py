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

def getPost(key):
	browser.get("https://twitter.com/login")
	browser.wait = WebDriverWait(browser, 15)
	try:
		username = browser.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(2) input")))
		username=browser.find_element_by_css_selector('#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(2) input')
		username.send_keys("marmeamaya")
	except NoSuchElementException:
		username = ""
	try:
		passwords =browser.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(3) > input")))
		passwords=browser.find_element_by_css_selector('#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(3) > input')
		passwords.send_keys("maya7733")

	except NoSuchElementException:
		passwords = ""

	try:
		browser.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "form > div.clearfix > button")))
		browser.find_element_by_css_selector("form > div.clearfix > button").click()
		time.sleep(4)
	except NoSuchElementException:
		print "cannot login"

	try:
		url='https://twitter.com/search?q=%40'+key+'&src=typd'
		browser.get(url)
		browser.wait = WebDriverWait(browser, 15)
	except NoSuchElementException:
		print "not found"
	try:
		goto=browser.find_element_by_css_selector(".ProfileCard-userFields > div > div > a").get_attribute("href")
		browser.get(goto)
		browser.wait = WebDriverWait(browser, 10)
	except NoSuchElementException:
		print "not found"	
	try:
		link=[]
		more=browser.find_elements_by_css_selector('a.tweet-timestamp.js-permalink.js-nav')	
		count_link = 0
		for i in more:
			if count_link < 5:
				getmore=i.get_attribute('href')
				link.append(getmore)
				#value["get_name"].append(get_name)
				print getmore
				count_link = count_link + 1
			else:
				more = "not found more"
		for a in link:
			browser.get(a)
			time.sleep(2)
			try:
				username=getElementAttr('span.username.js-action-profile-name > b',"textContent",browser)
				print "author_user = "+username
				profile_url=getElementAttr('a.account-group ',"href",browser)
				print "Profile URL = " +profile_url
				tweet_text=getElementAttr('p.js-tweet-text','textContent',browser)
				print "Text post = " +tweet_text
			except NoSuchElementException:
				print "Not found"
			try:
				url_post=browser.find_element_by_css_selector(".time a").get_attribute("href")
				print "Link = "+url_post
			except NoSuchElementException:
				url_post=""
			try:
				number_retweet=browser.find_element_by_css_selector('button.js-actionRetweet').get_attribute("textContent")
				print number_retweet
			except NoSuchElementException,e:
				number_retweet=''
			try:
				number_favorite=browser.find_element_by_css_selector('button.js-actionFavorite').get_attribute("textContent")
				print  number_favorite
			except NoSuchElementException,e:
				number_favorite=''
			try:
				imageUrl=browser.find_element_by_css_selector(' div > img').get_attribute("src")
				print "url_img "+ imageUrl
			except NoSuchElementException:
				imageUrl=''
			try:
				location=browser.find_element_by_css_selector('div.tweet-geo-text a.js-geo-pivot-link').get_attribute('textContent')
				print "location "+location
			except NoSuchElementException:
				location = ""
			try:
				date = browser.find_element_by_css_selector('div.client-and-actions span span').get_attribute('textContent')
				print date
			except NoSuchElementException:
				date =""
			
			try:
				value={
					"get_name":[],
					"get_time":[],
						"get_comment":[]
				}
				comment=browser.find_elements_by_css_selector('div.tweet.js-stream-tweet.js-actionable-tweet.js-profile-popup-actionable')
				count =0 
				for i in comment:
					if count < 5:
						try:
							get_name=i.find_element_by_css_selector('div.content > div.stream-item-header a strong').get_attribute('textContent')
							print get_name
						except NoSuchElementException:
							get_name = ""
						try:
							get_time=i.find_element_by_css_selector('div.content > div.stream-item-header > small > a > span').get_attribute('textContent')
							print get_time
						except NoSuchElementException:
							get_time = ""
						try:
							get_comment=i.find_element_by_css_selector('div > div.content > p').get_attribute('textContent')
							print get_comment
						except NoSuchElementException:
					
							comment = ""
						value["get_name"].append(get_name)
						value["get_time"].append(get_time)
						value["get_comment"].append(get_comment)
						count=count + 1
					else:
						comment= "none"
				obj = {
				"username":username,
				"profile_url":profile_url,
				"tweet_text":tweet_text,
				"url_post":url_post,
				"number_retweet":number_retweet,
				"number_favorite":number_favorite,
				"imageUrl":imageUrl,
				"location":location,
				"date":date,
				"comment":{
					"username":value["get_name"],
					"datetime":value["get_time"],
					"comment_text":value["get_comment"]
				}
				}

				myStr=json.dumps(obj)
				#print myStr
				nameFile="post_data.json"
				fs = open(nameFile, 'a')
				fs.write(myStr+"\n")

			except NoSuchElementException,e:
				number_comment=''

	except NoSuchElementException:
		print "not found more "


key=sys.argv[1]
getPost(key)
browser.quit()

