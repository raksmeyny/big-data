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
import traceback
from time import gmtime, strftime
import csv
reload(sys)
sys.setdefaultencoding("UTF8")
#browser=webdriver.Firefox()
profile_url=' '


# path_to_chromedriver = '/Users/djisse/Documents/cheerio/chromedriver' # change path as needed
# browser = webdriver.Chrome(executable_path = path_to_chromedriver)
browser = webdriver.Firefox()

def getSearchDetailAfter(url):
	browser.get(url)
	#fs = io.open('data_search_detail.csv', 'a', encoding='utf8')
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
	except NoSuchElementException:
		like_nb = ""
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
				print getcommenttext
				value["getcommenttext"].append(getcommenttext)
		else:
			for l in getamoutcomment:
				getcommenttext=l.get_attribute("textContent")
				print getcommenttext
				value["getcommenttext"].append(getcommenttext)
	except NoSuchElementException:
		getamoutcomment = ""
	
	obj = {
	
	"username":username,
	"datetime":getdate,
	"title":gettitle,
	"like_nb":like_nb,
	"detail_url":url,
	"comment":value["getcommenttext"]
	}
	
	myStr=json.dumps(obj)
	nameFile="searchafter_detail.json"
	fs = open(nameFile, 'a')
	fs.write(myStr+"\n")

try:
	url=sys.argv[1]
	getSearchDetailAfter(url)
	browser.quit()
except:
	print "Error script "
	traceback.print_exc()
	browser.quit()
	