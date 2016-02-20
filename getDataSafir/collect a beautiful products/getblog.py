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
	product_name=product_name.encode("utf-8")
	product = product_name + " blog review"
	browser.get("https://www.google.com/search?q="+product)
	print "https://www.google.com/search?q="+product
	#box = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "hplogo")))

	# try:	
	result= browser.find_elements_by_css_selector("h3 > a")
	#print result
	for i in result:
		linkProduct = i.get_attribute('href')
		#print linkProduct

		file_name = product_name+'.txt'
		script_dir = os.path.dirname(os.path.abspath(__file__))
		dest_dir = os.path.join(script_dir,product_name)
		try:
		    os.makedirs(dest_dir)
		except OSError:
		    pass # already exists
		path = os.path.join(dest_dir, file_name)
		with open(path, 'a') as stream:
		    stream.write(linkProduct+'\n')
	# except NoSuchElementException:
	# 	print "No result"

# try:
product_name=sys.argv[1]
product_name=product_name.encode('utf-8')
print product_name
searching(product_name)
browser.quit()
