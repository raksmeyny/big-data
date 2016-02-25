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
import json

reload(sys)
sys.setdefaultencoding("UTF8")
browser=webdriver.Firefox()

def searching(product_name):
	browser.get("http://www.digikala.com/Product/DKP-99869/Alcatel-Onetouch-2004C-Mobile-Phone/%DA%AF%D9%88%D8%B4%D9%8A-%D9%85%D9%88%D8%A8%D8%A7%D9%8A%D9%84-%D8%A2%D9%84%DA%A9%D8%A7%D8%AA%D9%84-%D9%85%D8%AF%D9%84-Onetouch-2004C#!/displaycomment-0/page-1/sort-date/tab-comments/")
	
	try:
		result= browser.find_elements_by_css_selector("div.content-panel.right > div > p")
		for i in result:
			commemt = i.get_attribute('textContent')
			obj = {
			"commemt":commemt
			}
			myStr=json.dumps(obj)
			nameFile="comment.json"
			fs = open(nameFile, 'a')
			fs.write(myStr+",\n")
		
	except NoSuchElementException:
		print "It doesn't get!!!"

product_name=sys.argv[1]
product_name=product_name.encode('utf-8')
searching(product_name)
browser.quit()
