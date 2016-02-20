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
browser=webdriver.Firefox()
#path_to_chromedriver = 'E:/Jibril-Project/facebook/chromedriver.exe'
# browser = webdriver.PhantomJS()
def getdesignname (url):
	browser.get(url)
	linkproduct=url.rsplit('/',1)[-1]
	cuturl = linkproduct.replace(".html","")
	browser.wait = WebDriverWait(browser, 50)
	fs = io.open('link.csv', 'a', encoding='utf8')
	try:
		getcoutryname = browser.find_element_by_css_selector("#col1 > div> p > a:nth-child(1) b").get_attribute("textContent")
	except NoSuchElementException:
		print "not found country"
	try:
		brandlink=browser.find_element_by_css_selector("#col1 > div > p > a:nth-child(5) ").get_attribute("href")
	except NoSuchElementException:
		brandlink=''
		print "not found brand"
	try:
		getbrandtitle = browser.find_element_by_css_selector("#col1 > div:nth-child(3) > img").get_attribute("alt")
		cutgetbrandtitle=getbrandtitle.replace("Logo","")
		databrand = getcoutryname+";"+brandlink+";"+cutgetbrandtitle+"\n"
		fs.write(databrand)
	except NoSuchElementException:
		print "not found title"

	try:
		getlinkproduct = browser.find_elements_by_css_selector("#col1 > div div  p > a")
		ds = io.open('linktoproduct.csv', 'a', encoding='utf8')
		for l in getlinkproduct:
			linktoproduct =l.get_attribute("href")
			ds.write(linktoproduct+"\n")

	except NoSuchElementException:
		print "not found title"

try:
	url=sys.argv[1]
	getdesignname(url)	
 	browser.quit()
except:
	print "Error script "
	browser.quit()
