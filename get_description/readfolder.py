import csv
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
from selenium.webdriver.support.ui import Select
import urllib
import re
import os
reload(sys)
sys.setdefaultencoding("UTF8")
browser=webdriver.Firefox()

def openfolder(foldername):
	productname=foldername
	f=open(productname+"/"+productname+".txt",'r')
	for url in f:
		browser.get(url)
		browser.wait = WebDriverWait(browser, 40)
		try:
			result= browser.find_elements_by_css_selector("div p")
			for i in result:
				try:
					paragraph = i.get_attribute('textContent')
					print paragraph

					fs = io.open(productname+"/"+productname+".csv", 'a', encoding = 'UTF8')
					fs.write(paragraph+"\n")

					print "can create file "
				except NoSuchElementException:
					print "No text"
		except NoSuchElementException:
			print "No result of p!"
		time.sleep(2)
try:
	foldername=sys.argv[1]
	openfolder(foldername)
	browser.close()
except NoSuchElementException:
	print "Error"
	browser.close()