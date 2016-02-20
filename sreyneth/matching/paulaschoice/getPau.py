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


def searching(product_name):
	browser.get("https://www.google.com/")
	box = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "hplogo")))

	try:
		search=browser.find_element_by_css_selector("div#gs_lc0 input#lst-ib")
		product=product_name.replace("_"," ")
		re = product + " review" + " beautypedia"
		search.send_keys(re)
	except NoSuchElementException:
		print "cannot search"
		return -1

	try:
		clicksearch = browser.find_element_by_css_selector("div.jsb center input:nth-child(1)")
		clicksearch.click()
	except NoSuchElementException:
		print "dosen't click search!"
	time.sleep(4)
	try:
		firstlink=browser.find_elements_by_css_selector('#rso > div > div > div > h3 a')
		
		obj=[]
		for g in firstlink:
			url=g.get_attribute("href")
			mystring=str(url)
			
			myurl=mystring.find("http://www.paulaschoice.com/beautypedia-skin-care-reviews/")
			m = mystring.find('_/')
			print m
			if myurl != -1 and m != -1:
				obj.append(url)
				link = io.open('link.csv', 'a', encoding='utf8')
				link.write(url+"\n")
			else:
				print "another website"
		for g in obj:
			print g
			l=str(g)
			browser.get(l)
			time.sleep(4)

	except NoSuchElementException:
		firstlink = ""
		
try:
	product_name=sys.argv[1]
	b=searching(product_name)
	browser.quit()
except NoSuchElementException:
	browser.quit()
	print "Error"