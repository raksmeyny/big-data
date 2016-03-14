import time
import datetime
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
reload(sys)
sys.setdefaultencoding("UTF8")
browser = webdriver.Firefox()
# path_to_chromedriver = 'E:/Jibril-Project/facebook/chromedriver.exe'
# browser = webdriver.Chrome(executable_path = path_to_chromedriver)
arrlink=[]
def getPost(key):
	url='https://instagram.com/'+key
	browser.get(url)
	now = datetime.datetime.now()
	scrapingdate=now.isoformat()
	try:
		fullname=browser.find_element_by_css_selector('h2._79dar').get_attribute("textContent")
	except NoSuchElementException:
		fullname=''
		print "fullname not found"
	try:
		bio=browser.find_element_by_css_selector("div._bugdy > span> span").get_attribute("textContent")
	except NoSuchElementException:
		print "bio not found"
		bio=''
	try:
		website=browser.find_element_by_css_selector("div._bugdy a._56pjv").get_attribute("href")
	except NoSuchElementException:
		print "website not found"
		website=''
	try:
		nbPost=browser.find_element_by_css_selector("span._e8fkl").get_attribute("textContent")
	except NoSuchElementException:
		print "number of Post not found"
	try:
		nbFollower=browser.find_element_by_css_selector("span._pr3wx").get_attribute("textContent")
	except NoSuchElementException:
		print "number of Follower not found"
		nbFollower=""

	try:
		nbFollwing=browser.find_element_by_css_selector("span._bgvpv").get_attribute("textContent")
	except NoSuchElementException:
		print "number of Following not found"
		nbFollwing=''
	try:
		post1=browser.find_element_by_css_selector(" div > div._nljxa > div._myci9:first-child >a:nth-child(1)").get_attribute("href")
		arrlink.append(post1)
	except NoSuchElementException:
		print "cannot link1"
		post1=''
	try:
		post2=browser.find_element_by_css_selector(" div > div._nljxa > div._myci9:first-child >a:nth-child(2)").get_attribute("href")
		arrlink.append(post2)
	except NoSuchElementException:
		print "cannot link2"
		post2=''
	if(key):
		fs = io.open('profile-info.csv', 'a', encoding='utf8')
		result=str(key)+","+str(fullname)+","+str(bio)+","+str(website)+","+str(nbPost)+","+str(nbFollower)+","+str(nbFollwing)+","+str(post1)+","+str(post2)+","+str(url)+"\n"
		fs.write(result.decode())
	try:
		
		for h in arrlink:
			browser.get(h)
			time.sleep(3)
			try:
				postdesc=browser.find_element_by_css_selector("li._nk46a h1> span").get_attribute("innerHTML")
				postdesc=re.sub(r'\<[^>]*\>', r'', postdesc)
				print "============================"
				print postdesc.encode("utf-8")
				print "==========================="
			except NoSuchElementException:
				print "No description Post"
			try:
				nblike=browser.find_element_by_css_selector("span._tf9x3 span:nth-child(2)").get_attribute("textContent")
			except NoSuchElementException:
				print "Number like Not found"
				nblike=''
			try:
				datepost=browser.find_element_by_css_selector("time._379kp").get_attribute("datetime")
			except NoSuchElementException:
				print "No date "
			try:
				nbcomment=browser.find_element_by_css_selector("button._l086v._ifrvy span:nth-child(2)").get_attribute("textContent")
			except NoSuchElementException:
				print "Number Comment Not found"
				try:
					getComment=browser.find_elements_by_css_selector("ul li._nk46a:not(:first-child)")
					nbcomment=len(getComment)
				except NoSuchElementException:
					nbcomment=''
			posts={
				"username":key,
				"fullname":fullname,
				"bio":bio,
				"website":website,
				"postDesc":postdesc,
				"datepost":datepost,
				"numberPost":nbPost,
				"numberFollwer":nbFollower,
				"numberFollwing":nbFollwing,
				"url":h,
				"numberLike":nblike,
				"numberComment":nbcomment,
				"scrapingdate":scrapingdate,
				"comments":[]	
			}
			
			for d in range(10):
				try:
					btnLoadMore=browser.find_element_by_css_selector("button._l086v._ifrvy")
					btnLoadMore.click()
					time.sleep(4)
				except NoSuchElementException:
					print 'load more not found'
			try:
				getComment=browser.find_elements_by_css_selector("ul li._nk46a:not(:first-child)")
				for comm in getComment:
					try:
						username=comm.find_element_by_tag_name('a').get_attribute("textContent")
						textComment=comm.find_element_by_css_selector('span > span').get_attribute("textContent")
						print username
						print textComment.encode('utf-8')
						obj={
							"username":username,
							"textComment":textComment
						}
						posts["comments"].append(obj)

					except NoSuchElementException:
						print "username  Not found"
				data=json.dumps(posts)
				nameFile="allPost.json"
				fs = open(nameFile, 'a')
				# fs.write("["+data+"],"+"\n")
				fs.write(data+"\n")
			except NoSuchElementException:
				print "Comment Not found"
		
	except NoSuchElementException:
		print "not found post"

try:
	key=sys.argv[1]
	if key!='':
		getPost(key)
		browser.quit()
	else:
		print "key is empty"
except:
	print "Error Script"
	browser.quit()
