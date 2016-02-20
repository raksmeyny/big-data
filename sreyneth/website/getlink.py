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
pros = ""
cons=""
best_uses=""
browser = webdriver.Firefox()

def getUserProfile():
		url="http://www.paulaschoice.com/beautypedia"
		browser.get(url)
		browser.wait = WebDriverWait(browser, 30)
		try:
			skincare=browser.find_elements_by_css_selector('#submenu-skincare > div > div > div > a.submenu-item')
			for i in skincare:
				getskincare=i.get_attribute('href')
				print getskincare
				# l = io.open('menu.csv', 'a', encoding='utf8')
				# l.write(getskincare+"\n")
		except NoSuchElementException:
			skincare = ""
		try:
			makeup=browser.find_elements_by_css_selector('#submenu-makeup > div > div > div > a.submenu-item')
			for i in makeup:
				getmakeup=i.get_attribute('href')
				print getmakeup
				link = io.open('menu.csv', 'a', encoding='utf8')
				link.write(getmakeup+"\n")
		except NoSuchElementException:
			makeup = ""	
				
try:
	getUserProfile()
	browser.quit()
except:
	print "Error script "
	traceback.print_exc()
	browser.quit()