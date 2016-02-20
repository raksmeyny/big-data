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
		url="http://www.paulaschoice.com/beautypedia-skin-care-reviews/by-brand/becca/_/Ever-Matte-Poreless-Priming-Perfector"
		browser.get(url)
		browser.wait = WebDriverWait(browser, 30)
		try:
			brand_name=browser.find_element_by_css_selector('#brand-link-desktop').get_attribute('textContent')
			print brand_name
		except NoSuchElementException:
			brand_name = ""
		try:
			product_name=browser.find_element_by_css_selector('div.product-name').get_attribute("textContent")
			print product_name
		except NoSuchElementException:
			product_name = " "	
		try:
			price_size=browser.find_element_by_css_selector('div.price.and-size').get_attribute("textContent")
			print price_size
		except NoSuchElementException:
			price_size = " "
		try:
			expert_rat=browser.find_element_by_css_selector('div.rating.upper.expert.rating-100').get_attribute("class")
			print expert_rat
		except NoSuchElementException:
			expert_rat = " "
		try:
			com_rat=browser.find_element_by_css_selector('div.rating.upper.community.rating-70').get_attribute("class")
			print com_rat
		except NoSuchElementException:
			com_rat = " "	
		try:
			like=browser.find_element_by_css_selector('div.comment-numbers > div').get_attribute("textContent")
			print like
		except NoSuchElementException:
			like = " "
		try:
			box_pro=browser.find_elements_by_css_selector('#pr-header-23772 > div.pr-snapshot > div.pr-snapshot-body > div > div.pr-review-points > div')
			for f in box_pro:
				try:
					pro=f.find_element_by_css_selector('div.pr-attribute-group.pr-rounded.pr-attribute-pros> div.pr-attribute-value > div').get_attribute('textContent')
					print pro
				except NoSuchElementException:
					pro = ""
				try:
					con=f.find_element_by_css_selector('div.pr-attribute-group.pr-rounded.pr-attribute-cons> div.pr-attribute-value > div').get_attribute('textContent')
					print con
				except NoSuchElementException:
					con = ""
				try:
					best_use=f.find_element_by_css_selector('div.pr-attribute-group.pr-rounded.pr-attribute-bestuses.pr-last> div.pr-attribute-value > div').get_attribute('textContent')
					print best_use
				except NoSuchElementException:
					best_use = ""
		except NoSuchElementException:
			box_pro = ""
		try:
			percent=browser.find_element_by_css_selector('p.pr-snapshot-consensus-value.pr-rounded').get_attribute('textContent')
			print percent
		except NoSuchElementException:
			percent = ""
		try:
			skin_tone=browser.find_element_by_css_selector('li.pr-other-attribute-value').get_attribute('textContent')
			print skin_tone
		except NoSuchElementException:
			skin_tone = ""
		try:
			review=browser.find_elements_by_css_selector('#pr-contents-23772 > div > div')
			for i in review:
				try:
					by=i.find_element_by_css_selector('p.pr-review-author-name > a > span').get_attribute('textContent')
					print by
				except NoSuchElementException:
					by = ""
				try:
					date=i.find_element_by_css_selector('div.pr-review-author-date.pr-rounded').get_attribute('textContent')
					print date
				except NoSuchElementException:
					date = ""
				try:
					location=i.find_element_by_css_selector('p.pr-review-author-location > span').get_attribute('textContent')
					print location
				except NoSuchElementException:
					location = ""
				try:
					about_me=i.find_element_by_css_selector('div.pr-review-author-info-wrapper > div > p > span').get_attribute('textContent')
					print about_me
				except NoSuchElementException:
					about_me = ""
				try:
					box=i.find_elements_by_css_selector('div.pr-review-main-wrapper > div.pr-review-points > div')
					for a in box:
						try:
							pros=a.find_element_by_css_selector('div.pr-attribute-group.pr-rounded.pr-attribute-pros').get_attribute('textContent')
							print pros
						except NoSuchElementException:
							pros = ""
						try:
							cons=a.find_element_by_css_selector('div.pr-attribute-group.pr-rounded.pr-attribute-cons').get_attribute('textContent')
							print cons
						except NoSuchElementException:
							cons = ""
						try:
							best_uses=a.find_element_by_css_selector('div.pr-attribute-group.pr-rounded.pr-attribute-bestuses.pr-last').get_attribute('textContent')
							print best_uses
						except NoSuchElementException:
							best_uses = ""
				except NoSuchElementException:
					box = ""
				try:
					comment=i.find_element_by_css_selector('p.pr-comments').get_attribute('textContent')
					print comment
				except NoSuchElementException:
					comment = ""
				try:
					st=i.find_element_by_css_selector('li.pr-other-attribute-value').get_attribute('textContent')
					print st
				except NoSuchElementException:
					st = ""
				try:
					bottom_line=i.find_element_by_css_selector('div.pr-review-bottom-line-wrapper > p').get_attribute('textContent')
					print bottom_line
				except NoSuchElementException:
					bottom_line = ""
				try:
					cus_found=i.find_element_by_css_selector('div.pr-review-most-helpful > p > span').get_attribute('textContent')
					print cus_found
				except NoSuchElementException:
					cus_found = ""
				# if by == "":
				# 	print "Review not found"
				# else:
				# 	obj={
				# 	"Username":by,
				# 	"Date":date,
				# 	"From":location,
				# 	"About_me":about_me,
				# 	"Text_Comment":comment,
				# 	"Skin_Tone":st,
				# 	"Bottom_Line":bottom_line,
				# 	"Customer_found":cus_found,
				# 	"Pros":pros,
				# 	"Cons":cons,
				# 	"Best Uses":best_uses
				# 	}
				# 	myStr=json.dumps(obj)
				# 	nameFile="review.json"
				# 	fs = open(nameFile, 'a')
				# 	fs.write(myStr + ",\n")
		except NoSuchElementException:
			review = " "
		# obj={
		# "Brand_name":brand_name,
		# "Product_name":product_name,
		# "Price_Size":price_size,
		# "Number_of_like":like,
		# "Skin_Tone":skin_tone,
		# "Percentag":percent,
		# "Expert_rating":expert_rat,
		# "community_rating":com_rat,
		# "Pros":pro,
		# "Cons":con,
		# "Best Uses":best_use
		# }
		# myStr=json.dumps(obj)
		# nameFile="product.json"
		# fs = open(nameFile, 'a')
		# fs.write(myStr + ",\n")
try:
	getUserProfile()
	browser.quit()
except:
	print "Error script "
	traceback.print_exc()
	browser.quit()