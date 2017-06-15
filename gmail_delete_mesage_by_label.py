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

def findUnreadCount(label):
    if label is None:
        return 0
    else:
        arr = label.split(' ')
        return int(str(arr[1]))

def findLabel(driver, labelName):
    labelElem = driver.find_element_by_xpath('//a[@href="https://mail.google.com/mail/u/0/#label/' + labelName + '"]')
    return labelElem.get_attribute('aria-label')

def deleteEmails(driver):
    unread = findUnreadCount(findLabel(labelName))
    while (unread > 0):
        checkElems=driver.find_elements_by_xpath('//*[@aria-checked="false"]')
        allCheck=checkElems[9]
        allCheck.click()
        print('Selecting all email on the screen')
        time.sleep(2)
        delElem=driver.find_element_by_xpath('//*[@aria-label="Delete"]')
        delElem.click()
        print('Deleting selected emails on the screen')
        time.sleep(5)
        unread = findUnreadCount(findLabel(labelName))
        if label is None:
            unread=0
        else:
            arr=label.split(' ')
            unread=int(str(arr[1]))
        print('Remaining unread: ' + str(unread))


