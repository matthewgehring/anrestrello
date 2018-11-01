import urllib.request
from bs4 import BeautifulSoup
import requests
import random
key = "f5b27409aaeb693cdd28d15cd63c8474"
token = "5c342876d76de7617084008db01841cb252018a11462ae4968df20403c78160b"


contents = urllib.request.urlopen("https://anresco.qbench.net/samples").read()
soup = BeautifulSoup(contents, 'html.parser')
#print(soup)

def makeCard(sampleId, dueDate):
    sample = sampleId
    date = dueDate
    url = "https://api.trello.com/1/cards"

    querystring = {"name":sample,"due":date,"idList":"5bc5208dae8fe9286f8089b1","keepFromSource":"all","key":"f5b27409aaeb693cdd28d15cd63c8474","token":"5c342876d76de7617084008db01841cb252018a11462ae4968df20403c78160b"}

    response = requests.request("POST", url, params=querystring)

    print(response.text)

#print(response.text)

def makeChecklist(tests):
    #tests = tests;

    url = "https://api.trello.com/1/cards/5bc62cc6482e0b4bc2a67ad3/checklists"

    querystring = {"name":"Tests","key":"f5b27409aaeb693cdd28d15cd63c8474","token":"5c342876d76de7617084008db01841cb252018a11462ae4968df20403c78160b"}

    response = requests.request("POST", url, params=querystring)




#def getSampleId():

#def getTests():

def unitTest():
    rand = str(random.randint(1,1000))
    makeCard("1999" + rand, "2018-10-01")

unitTest()

    

#make card
#make tests checklist
#get sample id
#get tests
