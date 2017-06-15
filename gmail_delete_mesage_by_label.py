import os
from selenium import webdriver

chromedriver = './chromedriver'
os.environ['webdriver.chrome.driver'] = chromedriver

driver = webdriver.Chrome(chromedriver)
driver.get('https://mail.google.com')
