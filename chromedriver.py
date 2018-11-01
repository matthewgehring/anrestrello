from selenium import webdriver
from bs4 import BeautifulSoup
import time
from tkinter import Tk
from selenium.webdriver.common.keys import Keys
import sqlite3
import database
driver = webdriver.Chrome('c:/Users/matthew/Desktop/Trello/chromedriver2.exe')
#database.openDataBaseConnection()
#database.unitTest()
#database.displayDataBase()
#database.closeDataBaseConnection()
def login():
    driver.get("https://anresco.qbench.net/")
    google = driver.find_element_by_id("qbenchGoogleLoginLink")
    google.click()
    email = driver.find_element_by_class_name("whsOnd")
    email.send_keys("matthew.anresco@gmail.com")
    email.send_keys(Keys.RETURN)
    time.sleep(1)
    password = driver.find_element_by_class_name("zHQkBf")
    password.send_keys("An8221101")
    password.send_keys(Keys.RETURN)
    time.sleep(1)


def getOrders():
    driver.get("https://anresco.qbench.net/orders")
    orders = []
    orders = driver.find_elements_by_xpath("//a[contains(@href, '/order?id=')]")
    x = 0
    while x < len(orders):
        print(orders[x].text)
        x += 1

def getMostRecentOrder():
    driver.get("https://anresco.qbench.net/orders")
    order = driver.find_element_by_xpath("//a[contains(@href, '/order?id=')]")
    return order.text

def getOrderSamples(order):
    driver.get("https://anresco.qbench.net/order?id=" + "502663")
    time.sleep(1)
    samples = []
    samplesText = []
    samples = driver.find_elements_by_xpath("//a[contains(@href, '/sample?id=')]")
    x = 0
    while x < len(samples):
        samplesText.append(samples[x].text)
        x += 1
    print(samplesText)

def getTests(sampleID):
    driver.get("https://anresco.qbench.net/sample?id=" + "1011565")
    time.sleep(1)
    tests = []
    testText = []
    table = driver.find_element_by_class_name("table")
    rows = table.find_elements_by_tag_name("td")
    x = 2
    while x < len(rows):
        testText.append(rows[x].text)
        x += 4
    return testText

def getDueDate(order):
    driver.get("https://anresco.qbench.net/order?id=" + order)
    time.sleep(1)
    date = driver.find_element_by_id("qbenchOrderDateRequired")
    date.send_keys(Keys.CONTROL + "a")
    date.send_keys(Keys.CONTROL + "c")
    time.sleep(1)
    date = Tk().clipboard_get()
  
    return date
#def addOrderToDB():
    #add order number to db
    
#def checkDB():
    #check db file

#def mainLoop():
    #get order
    #check text file
    #add to text file
    #get samples
    #get tests
    #send to trello

    
login()
#getOrders()
time.sleep(1)
#getOrderSamples(getMostRecentOrder())
#getTests(0)
#time.sleep(5)
#getDueDate(100)
#driver.quit()
