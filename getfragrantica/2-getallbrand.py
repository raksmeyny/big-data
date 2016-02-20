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
import re
from selenium.webdriver.support.ui import Select
import urllib
import csv
reload(sys)
sys.setdefaultencoding("UTF8")
browser = webdriver.Firefox()

def getLinkProduct (url):
	browser.get(url)
	browser.wait = WebDriverWait(browser,15)
	fs = io.open('getlinkproduct.csv', 'a', encoding='utf8')
	try:
		allProductImg=browser.find_elements_by_css_selector("div.nduList>p>a")
		for l in allProductImg:
			result=l.get_attribute("href")
			print "got it"
			fs.write(result+"\n")
	except NoSuchElementException:
		print "not found"
	
try:
	url=sys.argv[1]
	getLinkProduct(url)
 	browser.quit()
except:
	print "Error script "
	browser.quit()
