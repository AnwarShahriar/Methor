import os
import getpass
from selenium import webdriver

username = raw_input('Enter Gmail email: ')
password = getpass.getpass('Enter Gmail password: ')
label = raw_input('Enter the Label you want to delete: ')

chromedriver = './chromedriver'
os.environ['webdriver.chrome.driver'] = chromedriver

driver = webdriver.Chrome(chromedriver)
driver.get('https://mail.google.com')
