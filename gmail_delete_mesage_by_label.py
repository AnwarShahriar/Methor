import os
import getpass
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

username = raw_input('Enter Gmail email: ')
password = getpass.getpass('Enter Gmail password: ')
labelName = raw_input('Enter the Label you want to delete: ')

chromedriver = './chromedriver.exe' if sys.platform == 'win32' else './chromedriver'
os.environ['webdriver.chrome.driver'] = chromedriver

def login(driver, username, password):
    time.sleep(5)

    usernameElem = driver.find_element_by_id('identifierId')
    usernameElem.send_keys(username)
    usernameElem.send_keys(Keys.ENTER)

    time.sleep(3)

    passwordElem = driver.find_element_by_name('password')
    passwordElem.send_keys(password)
    passwordElem.send_keys(Keys.ENTER)

def loadUrl(driver, url):
    time.sleep(5)
    driver.get(url)
    time.sleep(5)

def hasMoreMessage(driver):
    try:
        labelElems = driver.find_element_by_id(':2').find_element_by_xpath('//td[@class="TC"]')
        if labelElems.get_attribute('class') == 'TC':
            return False
        else:
            return True
    except Exception:
        return True

def deleteEmails(driver):
    moreMessage = hasMoreMessage(driver)
    while (moreMessage):
        checkElems=driver.find_element_by_id(':5').find_elements_by_xpath('//span[@aria-checked="false"]')
        allCheck=checkElems[-1]
        allCheck.click()
        print('Selecting all email on the screen')
        time.sleep(2)
        delElem=driver.find_element_by_xpath('//*[@aria-label="Delete"]')
        delElem.click()
        print('Deleting selected emails on the screen')
        time.sleep(5)
        moreMessage = hasMoreMessage(driver)
    print('All email deleted in ' + labelName + ' label')

def generateUrl(labelName):
    defaults = {
        'Inbox': 'inbox',
        'Starred': 'starred',
        'Sent Mail': 'sent',
        'Drafts': 'drafts'
    }
    categories = ['Social', 'Promotions', 'Updates', 'Forums']
    
    if labelName in categories:
        url = 'https://mail.google.com/mail/u/0/#category/' + labelName.lower()
    elif labelName in defaults.keys():
        url = 'https://mail.google.com/mail/u/0/#' + defaults[labelName]
    else:
        arr = labelName.split(' ')
        urlPart = ''
        for index, part in enumerate(arr):
            urlPart += part
            if index != (len(arr) - 1):
                urlPart += '+'
        url = 'https://mail.google.com/mail/u/0/#label/' + urlPart
    
    return url

# Start Working
driver = webdriver.Chrome(chromedriver)
loadUrl(driver, 'https://mail.google.com')
login(driver, username, password)
time.sleep(10)
loadUrl(driver, generateUrl(labelName))
time.sleep(10)
deleteEmails(driver)