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
    unread = findUnreadCount(findLabel(driver, labelName))
    print('Remaining unread: ' + str(unread))
    while (unread > 0):
        checkElems=driver.find_element_by_id(':5').find_elements_by_xpath('//span[@aria-checked="false"]')
        allCheck=checkElems[-1]
        allCheck.click()
        print('Selecting all email on the screen')
        time.sleep(2)
        delElem=driver.find_element_by_xpath('//*[@aria-label="Delete"]')
        delElem.click()
        print('Deleting selected emails on the screen')
        time.sleep(5)
        unread = findUnreadCount(findLabel(driver, labelName))
        print('Remaining unread: ' + str(unread))


# Start Working
driver = webdriver.Chrome(chromedriver)
loadUrl(driver, 'https://mail.google.com')
login(driver, username, password)
loadUrl(driver, 'https://mail.google.com/mail/u/0/#label/' + labelName)
deleteEmails(driver)