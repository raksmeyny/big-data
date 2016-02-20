import time
import io
import sys
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium import selenium
import selenium 
import csv
from selenium.webdriver.support.ui import Select
import urllib
import re
import os

reload(sys)
sys.setdefaultencoding("UTF8")
browser=webdriver.Firefox()


def searching(product_name,numberOfPage):
	browser.get("https://www.google.com/")
	box = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "hplogo")))
	
	#fs = io.open('name.csv', 'a', encoding='utf8')

	try:
		search=browser.find_element_by_css_selector("div#gs_lc0 input#lst-ib")
		product=product_name.replace("_"," ")
		re = product + " review"
		search.send_keys(re)
	except NoSuchElementException:
		print "cannot search"
		return -1

	try:
		clicksearch = browser.find_element_by_css_selector("div.jsb center input:nth-child(1)")
		clicksearch.click()
	except NoSuchElementException:
		print "dosen't click search!"

	link=[]
	for n in range(0, numberOfPage):
		box = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "resultStats")))

		
		result= browser.find_elements_by_css_selector(".r a")
		for i in result:
			linkProduct = i.get_attribute('href')
			#print linkProduct
			link.append(linkProduct)


		nextnub=browser.find_element_by_css_selector("#pnnext")
		nextnub.click()
		box = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "resultStats")))
		time.sleep(2)
	return link

def openLink(link):
	for l in link:
		print l
		browser.get(l)
		time.sleep(4)
		html_sources = browser.page_source
		time.sleep(4)
		getblogs = html_sources.find("blog")


		if getblogs==-1:
			print "No found"
			continue
		if "fragrantica" in l:
			print "its youtube not blog"
			continue
		print "Word blog is found"

		file_name = product_name+'.txt'
		script_dir = os.path.dirname(os.path.abspath(__file__))
		dest_dir = os.path.join(script_dir,product_name)
		try:
		    os.makedirs(dest_dir)
		except OSError:
		    pass # already exists
		path = os.path.join(dest_dir, file_name)
		with open(path, 'a') as stream:
		    stream.write(l+'\n')

# try:
# 	product=sys.argv[1]
# 	b=searching(product)
# 	openLink(b)
# 	browser.quit()
# except:
# 	print "Error script "
# 	browser.quit()
try:
	product_name=sys.argv[1]
	b=searching(product_name,10)
	openLink(b)
	browser.quit()
except NoSuchElementException:
	browser.quit()
	print "Error"