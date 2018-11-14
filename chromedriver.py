from selenium import webdriver
from bs4 import BeautifulSoup
import time
from tkinter import Tk
from selenium.webdriver.common.keys import Keys
import sqlite3
import database
driver = webdriver.Chrome('c:/Users/matthew/Desktop/Trello/chromedriver2.exe')




order1 = [502535, 502632, 502675, 502685, 502708, 502711, 502712, 502713, 502715, 502718]
order2 = [502719, 502724, 502725, 502739, 502740, 502748, 502754, 502759, 502764, 502775, 502795]
order3 = [502805, 502815, 502828, 502846, 502832, 502854, 502855, 502878, 502704, 502625, 502650, 502665, 502618, 502517]
orders = [order1, order2, order3]


def login():
    driver.get("https://anresco.qbench.net/")
    google = driver.find_element_by_id("qbenchGoogleLoginLink")
    google.click()
    email = driver.find_element_by_class_name("whsOnd")
    email.send_keys("matthew.anresco@gmail.com")
    email.send_keys(Keys.RETURN)
    time.sleep(1)
    password = driver.find_element_by_class_name("zHQkBf")
    password.send_keys("")
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
    driver.get("https://anresco.qbench.net/order?id=" + order)
    time.sleep(1)
    samples = []
    samplesText = []
    samples = driver.find_elements_by_xpath("//a[contains(@href, '/sample?id=')]")
    x = 0
    while x < len(samples):
        samplesText.append(samples[x].text)
        x += 1
    return samplesText

def getTests(sampleID):
    driver.get("https://anresco.qbench.net/sample?id=" + sampleID)
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
def addToDB(order, samples, tests, dueDate):
    #add order to db
    database.openDataBaseConnection()
    database.addToDataBase(order, samples, tests, dueDate)
    database.displayDataBase()
    database.closeDataBaseConnection()
    
#def checkDB():
    #check db file

def mainLoop():
    #get order
    order = getMostRecentOrder()
    #get samples
    samples = getOrderSamples(order)
    #get tests
    try:
        tests = getTests(samples[0])
    except:
        order = str((int(order) - 1))
        samples = getOrderSamples(order)
        tests = getTests(samples[0])
    #get dueDate
    dueDate = getDueDate(order)
    #join list with pipe
    samples = "|".join(samples)
    tests = "|".join(tests)
    #add to database
    addToDB(order, samples, tests, dueDate)
    #check text file
    #add to text file
    #send to trello
def orderLoop(orders):
    for order in orders:
        for number in order:
            num = str(number)
            print(num + " is due: " + getDueDate(num))
    
login()
#getOrders()
time.sleep(5)
#mainLoop()
orderLoop(orders)
time.sleep(1)
#getOrderSamples(getMostRecentOrder())
#getTests(0)
#time.sleep(5)
#getDueDate(100)
driver.quit()
