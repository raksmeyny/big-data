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
from selenium.webdriver.support.ui import Select
import urllib

reload(sys)
sys.setdefaultencoding("UTF8")
browser=webdriver.Firefox()

def searching(Title):
	browser.get("http://www.fragrantica.com/")
	browser.wait = WebDriverWait(browser, 40)
	try:
		search=browser.find_element_by_css_selector("input#qajax")
		search.send_keys(Title);
		time.sleep(8)
		try:
			result= browser.find_element_by_css_selector("div#presultsajax p a:nth-child(1)")
			try:
				linkProduct = result.get_attribute('href')
				print linkProduct
				result.click()
				print "Click result"
			except NoSuchElementException:
				print "No link of product"
			try:
				title = browser.find_element_by_css_selector("div > div > h1 > span").get_attribute("textContent")
				print title
			except NoSuchElementException:
				print "No title of this product"
				title = "None"
			obj={
				"Link": linkProduct,
				"Title":title
			}		

			myStr=json.dumps(obj)
			myStr=myStr+', \n'
			print myStr
			
			#uniqlines = set(open('fragranticalink.json').readlines())
			#fs = open('fragranticalink.json', 'w').writelines(set(uniqlines))
			fs = open("fragranticalink.json", 'a')
			fs.write(myStr)

		except NoSuchElementException:
			print "No result of search!"
		print "get search"
	except NoSuchElementException:
		print "cannot search"
		return -1
	time.sleep(2)


with open('newTitle.json') as data_file:    
    data = json.load(data_file)

for line in data:
    #print line["title"]
    Title = line["title"]
    try:
    	searching(Title)
    except:
    	print "search not match!"
