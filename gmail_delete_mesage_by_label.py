import os
import getpass
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

username = raw_input('Enter Gmail email: ')
password = getpass.getpass('Enter Gmail password: ')
labelName = raw_input('Enter the Label you want to delete: ')

chromedriver = './chromedriver'
os.environ['webdriver.chrome.driver'] = chromedriver

driver = webdriver.Chrome(chromedriver)
driver.get('https://mail.google.com')

time.sleep(5)

usernameElem = driver.find_element_by_id('identifierId')
usernameElem.send_keys(username)
usernameElem.send_keys(Keys.ENTER)

time.sleep(3)

passwordElem = driver.find_element_by_name('password')
passwordElem.send_keys(password)
passwordElem.send_keys(Keys.ENTER)

time.sleep(5)

driver.get('https://mail.google.com/mail/u/0/#label/' + labelName)