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
profile_url=' '
date = ""
avg=""
username=''
browser = webdriver.Firefox()

def getUserProfile(url):
		
		browser.get(url)
		browser.wait = WebDriverWait(browser, 30)
		time.sleep(2)

		try:
			newurl=re.sub(r'(.*?\-reviews\/)(.*)', r'\1', url)
			print newurl
		except NoSuchElementException:
			perpage = ""
		try:
			getSort=browser.find_element_by_css_selector('#sort-control > div > select > option:nth-child(2)').get_attribute('value')
			print getSort
			sortnum=re.sub(r'(.*\d+\+\d+?\&)(.*)',r'\1',getSort)
			print sortnum
		except NoSuchElementException:
			getSort = ""
		try:
			link=[]
			page=browser.find_element_by_css_selector('div.page-number > span.total-pages').get_attribute('textContent')
			print page
			pageView = int(page)
			i = 0
			urlpage=''
			for l in range(pageView):

				urlpage = str(newurl)+str(sortnum)+"No="+str(i)+"&Ns=p_num_days_published%7C0"
				i = i + 24
				link.append(urlpage)
				print urlpage
			for g in link:
				try:
					browser.get(urlpage)
					print "start open product url"
					linkbox=browser.find_elements_by_css_selector('a.review-product')
					for i in linkbox:
						productUrl=i.get_attribute('href')
						print productUrl
						linkpro = io.open('product_url.csv', 'a', encoding='utf8')
						linkpro.write(productUrl+"\n")
						print "Finished with get link product"
				except NoSuchElementException:
					print  ""
		except NoSuchElementException:
			page = ""
		
		

				
try:
	key=sys.argv[1]
	getUserProfile(key)
	browser.quit()
except:
	print "Error script "
	traceback.print_exc()
	browser.quit()