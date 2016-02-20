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
import datetime
import re
import traceback
import utils
import json
from selenium.webdriver.support.ui import Select
reload(sys)
sys.setdefaultencoding("UTF8")
browser=webdriver.Firefox()

def scroll(url):
	try:
	    browser.wait = WebDriverWait(browser, 5)
	    browser.get(url)
	    browser.wait = WebDriverWait(browser, 5)
	    box = browser.wait.until(EC.presence_of_element_located((By.ID, "doc")))

	    for i in range(1,10):
	    	print "scrolling"
	    	browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	    	time.sleep(2)
	    print 'scrolling finish'
	    return 1
	except NoSuchElementException,e:
		print 'Error in scrolling of '+url+' :'
		print(traceback.format_exc())
	except TimeoutException,e:
		print 'Sroll: Time out for '+url+' :'

def getElementAttr(selector,attr,parent):
	try:
		elt=parent.find_element_by_css_selector(selector).get_attribute(attr)
		return elt
	except NoSuchElementException,e:
		print "element not found: "+selector
		return "-1"

def getUserProfile(key):
	browser.get("https://twitter.com/login")
	browser.wait = WebDriverWait(browser, 15)
	
	try:
		username = browser.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(2) input")))
		username=browser.find_element_by_css_selector('#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(2) input')
		username.send_keys("marmeamaya")
	except NoSuchElementException:
		username = ""

	try:
		passwords =browser.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(3) > input")))
		passwords=browser.find_element_by_css_selector('#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(3) > input')
		passwords.send_keys("maya7733")

	except NoSuchElementException:
		passwords = ""

	try:
		browser.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "form > div.clearfix > button")))
		browser.find_element_by_css_selector("form > div.clearfix > button").click()
		time.sleep(4)
	except NoSuchElementException:
		print "cannot login"
	try:
		url='https://twitter.com/search?q=%40'+key+'&src=typd'
		browser.get(url)
		browser.wait = WebDriverWait(browser, 15)
	except NoSuchElementException:
		print "not found"
	try:
		goto=browser.find_element_by_css_selector(".ProfileCard-userFields > div > div > a").get_attribute("href")
		browser.get(goto)
		browser.wait = WebDriverWait(browser, 10)
		try:
			username=browser.find_element_by_css_selector(".ProfileCardMini-screenname span").get_attribute("textContent")
			print "Username : "  +username
		except NoSuchElementException:
			username=''
		try:
			link_profile= browser.find_element_by_css_selector("a.account-group").get_attribute("href")
			print "Link profile : " +link_profile
		except NoSuchElementException:
			link_profile=''
		try:
			personal_web=browser.find_element_by_css_selector('.ProfileHeaderCard-urlText.u-dir a').get_attribute('textContent')
			print "Personal Web : " +personal_web
		except NoSuchElementException:
			personal_web=''
		try:
			url_avatar=browser.find_element_by_class_name("ProfileAvatar-image ").get_attribute("src")
			print "Url avatar : " +url_avatar
		except NoSuchElementException:
			url_avatar=''
		try:
			following_nb=browser.find_element_by_css_selector('li.ProfileNav-item--following span.ProfileNav-value').get_attribute("textContent")
			print "following number : "+following_nb
		except NoSuchElementException:
			following_nb=''
		try:
			follower_nb=browser.find_element_by_css_selector('li.ProfileNav-item--followers span.ProfileNav-value').get_attribute("textContent")
			print "follower number : " + follower_nb
		except NoSuchElementException:
			follower_nb=''
		try:
			bio_hashtags=browser.find_element_by_css_selector('p.ProfileHeaderCard-bio').get_attribute('textContent')
			print "Bio hashtags of user: " +bio_hashtags
		except NoSuchElementException:
			bio_hashtags = ""
		try:
			creation_date=browser.find_element_by_css_selector('span.ProfileHeaderCard-joinDateText').get_attribute('textContent')
			print "Jion date : " +creation_date
		except NoSuchElementException:
			creation_date=''
		try:
			location=browser.find_element_by_css_selector('span.ProfileHeaderCard-locationText').get_attribute('textContent')
			print "Location :" +location
		except NoSuchElementException:
			location=''
		try:
			favorite=browser.find_element_by_css_selector('.ProfileNav-item--favorites a span.ProfileNav-value').get_attribute('textContent')
			print "Favorite : " +favorite
		except NoSuchElementException:
			favorite=''
		try:
			post_nb=browser.find_element_by_css_selector('li.ProfileNav-item--tweets span.ProfileNav-value').get_attribute('textContent')
			print "Post number : " + post_nb
		except NoSuchElementException:
			post_nb =""

		try:
			value={
				"username":[],
				"profile_url":[],
				"tweet_text":[],
				"url_post":[],
				"number_favorite":[],
				"number_retweet":[],
				"imageUrl":[],
				"location":[],
				"date":[]
			}
			post = browser.find_elements_by_css_selector('div.tweet.original-tweet.js-original-tweet.js-stream-tweet.js-actionable-tweet')
			count_post = 0
			for f in post:
				if count_post < 5:
					try:
						username=getElementAttr('.username b',"textContent",f)
						print "Post author_user = "+username
						profile_url=getElementAttr('a.account-group ',"href",f)
						print "Profile URL = " +profile_url
						tweet_text=getElementAttr('p.js-tweet-text','textContent',f)
						print "Text post = " +tweet_text
					except NoSuchElementException:
						print "Not found"
					try:
						url_post=f.find_element_by_css_selector(".time a").get_attribute("href")
						print "Link = "+url_post
					except NoSuchElementException:
						url_post=""
					try:
						number_retweet=f.find_element_by_css_selector('button.js-actionRetweet').get_attribute("textContent")
						print "Post retweet number : " +number_retweet
					except NoSuchElementException,e:
						number_retweet=''
					try:
						number_favorite=f.find_element_by_css_selector('button.js-actionFavorite').get_attribute("textContent")
						print  "Post favorite number : " +number_favorite
					except NoSuchElementException,e:
						number_favorite=''
					try:
						imageUrl=f.find_element_by_css_selector(' div > img').get_attribute("src")
						print "Post url_img "+ imageUrl
					except NoSuchElementException:
						imageUrl=''
					try:
						location=f.find_element_by_css_selector('div.tweet-geo-text a.js-geo-pivot-link').get_attribute('textContent')
						print "Post location : "+location
					except NoSuchElementException:
						location = ""
					try:
						date = f.find_element_by_css_selector('div.client-and-actions span span').get_attribute('textContent')
						print date
					except NoSuchElementException:
						date =""
					value["username"].append(username)
					value["profile_url"].append(profile_url)
					value["tweet_text"].append(tweet_text)
					value["url_post"].append(url_post)
					value["number_favorite"].append(number_favorite)
					value["number_retweet"].append(number_retweet)
					value["imageUrl"].append(imageUrl)
					value["location"].append(location)
					value["date"].append(date)
					count_post=count_post + 1
				else:
					post = "none"
		except NoSuchElementException:
			post="none"

		try:
			value_follow={
			"getFollowingName":[],
			"getFollowerName":[]
			}
			print "Start following"
			following_url=browser.find_element_by_css_selector('li.ProfileNav-item.ProfileNav-item--following > a').get_attribute('href')
			browser.get(following_url)
			browser.wait = WebDriverWait(browser, 5)
			url = (browser.current_url)
			scroll(url)
			browser.wait = WebDriverWait(browser, 5)
			following_name=browser.find_elements_by_css_selector('div.ProfileCard-userFields > span > a > span')
			for b in following_name:
				getFollowingName=b.get_attribute('textContent')
				value_follow["getFollowingName"].append(getFollowingName)
				print getFollowingName
			print "Finished following"
		except  NoSuchElementException:
			following_url = ""
		try:
			
			print "Start follower"
			followers_url=browser.find_element_by_css_selector('li.ProfileNav-item.ProfileNav-item--followers > a').get_attribute('href')
			browser.get(followers_url)
			browser.wait = WebDriverWait(browser, 5)
			url = (browser.current_url)
			scroll(url)
			browser.wait = WebDriverWait(browser, 5)
			follower_name = browser.find_elements_by_css_selector('div.ProfileCard-userFields > span > a > span')
			for c in follower_name:
				getFollowerName=c.get_attribute('textContent')
				value_follow["getFollowerName"].append(getFollowerName)
				print getFollowerName
			print "finished follower"
		except NoSuchElementException:
			followers_url = ""

		try:
			link_favorite = browser.find_element_by_css_selector('li.ProfileNav-item.ProfileNav-item--favorites > a').get_attribute('href')
			browser.get(link_favorite)
			browser.wait = WebDriverWait(browser, 15)
		except NoSuchElementException:
			link_favorite = "none"
		try:
			value_fav={
				"favorite_username":[],
				"favorite_text":[]
			}
			print "Start find favorite post"
			user_favorite = browser.find_elements_by_css_selector('div.tweet.js-stream-tweet.js-actionable-tweet.js-profile-popup-actionable')
			count_name =0 
			for a in user_favorite:
				if count_name < 15:
					try:
						favorite_username=a.find_element_by_css_selector('a > span.username.js-action-profile-name > b').get_attribute('textContent')
						print favorite_username
					except NoSuchElementException:
						favorite_username = ""
					try:
						favorite_text=a.find_element_by_css_selector('div > div.content > p').get_attribute('textContent')
						print favorite_text
					except NoSuchElementException:
						favorite_text = ""

					value_fav["favorite_username"].append(favorite_username)
					value_fav["favorite_text"].append(favorite_text)

					count_name = count_name +1
				else:
					user_favorite= "No favorite found"
			print "Finished find favorite post"
		except NoSuchElementException:
			user_favorite = "none"
	except NoSuchElementException:
		print "link not found"
	obj = {
		"username":username,
		"link_profile":link_profile,
		"personal_web":personal_web,
		"url_avatar":url_avatar,
		"following_nb":following_nb,
		"follower_nb":follower_nb,
		"bio_hashtags":bio_hashtags,
		"location":location,
		"creation_date":creation_date,
		"post_nb":post_nb,
		"favorite_nb":favorite,
		"post":{
			"username":value["username"],
			"profile_url":value["profile_url"],
			"tweet_text":value["tweet_text"],
			"url_post":value["url_post"],
			"number_favorite":value["number_favorite"],
			"number_retweet":value["number_retweet"],
			"imageUrl":value["imageUrl"],
			"location":value["location"],
			"date":value["date"]
		},
		"favorite_post":{
			"favorite_username":value_fav["favorite_username"],
			"favorite_text":value_fav["favorite_text"]
		},
		"follower_Username":{
			"follower_name":value_follow["getFollowerName"],
			"following_name":value_follow["getFollowingName"]
		}
	}
	myStr=json.dumps(obj)
	nameFile="user_profile_data.json"
	fs = open(nameFile, 'a')
	fs.write(myStr+"\n")

key=sys.argv[1]
getUserProfile(key)

browser.quit()