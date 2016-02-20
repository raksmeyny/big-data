from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time
import re
import json
import datetime
import traceback
path_to_chromedriver = '/Users/djisse/Documents/cheerio/chromedriver' # change path as needed
import user
import utils
reload(sys)
sys.setdefaultencoding("UTF8")

browser = webdriver.Firefox()

def getUserProfileDetail(url):
	browser.get(url)
	#fs = io.open('getlike.csv', 'a', encoding='utf8')
	gettime=time.strftime("%Y-%m-%d %H:%M:%S")
	try:
		username = browser.find_element_by_css_selector('div > a._4zhc5._ook48').get_attribute('textContent')
		print username
	except NoSuchElementException:
		username = ""
	try:
		getdate=browser.find_element_by_css_selector(" section._54eek._56o5u > a > time").get_attribute("title")
		print gettime
	except NoSuchElementException:
		getdate = ""
	try:
		gettitle=browser.find_element_by_css_selector("div > article > div._es1du._rgrbt > ul > li:nth-child(1) > h1").get_attribute("textContent")
		print gettitle
	except NoSuchElementException:
		gettitle = ""
	try:
		like_nb=browser.find_element_by_css_selector("section._54eek._56o5u > div").get_attribute("textContent")
		print like_nb
		#return sum(int(like_nb)) / len(int(like_nb)) 
	except NoSuchElementException:
		like_nb = ""
	try:
		datelast_post=browser.find_element_by_css_selector('section._54eek._56o5u > a > time').get_attribute('title')
		print datelast_post
	except NoSuchElementException:
		datedatelast_post = ""
	try:
		getamoutcomment=browser.find_elements_by_css_selector("ul li._nk46a:not(:first-child)")
		# getamoutcomment[-10]
		allcomment=len(getamoutcomment)
		number=type(allcomment)
		chanum=str(allcomment)
		value = {
		
		"getcommenttext":[]
		}
		if allcomment >10:

			for l in getamoutcomment[:-10]:
				getcommenttext=l.get_attribute("textContent")
				value["getcommenttext"].append(getcommenttext)
		else:
			for l in getamoutcomment:
				getcommenttext=l.get_attribute("textContent")
				print getcommenttext
				value["getcommenttext"].append(getcommenttext)
	except NoSuchElementException:
		print "not found comment"

	
	obj = {
	
	"Post_username":username,
	"Date":getdate,
	"Description":gettitle,
	"Number_of_like":like_nb,
	"Link":url,
	"Comment":value["getcommenttext"]
	}
	
	myStr=json.dumps(obj)
	fs = open("post.json", 'a')
	fs.write(myStr+",\n")


try:
	url=sys.argv[1]
	getUserProfileDetail(url)
	browser.quit()
except:
	print "Error script "
	traceback.print_exc()
	browser.quit()
