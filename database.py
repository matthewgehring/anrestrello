import sqlite3

conn = sqlite3.connect('qbenchTEST.db')
#print ("Opened database successfully")

def createTable():
    #Table Start
    conn.execute('''CREATE TABLE QBENCHTEST
             (ID INTEGER PRIMARY KEY,
             ORDERNUMBER     TEXT    NOT NULL,
             SAMPLES         TEXT    NOT NULL,
             TESTS           TEXT    NOT NULL,
             DUEDATE         TEXT    NOT NULL,
             ONTRELLO        INT     NOT NULL);''')

    print ("Table created successfully")

def openDataBaseConnection():
    conn = sqlite3.connect('qbenchTEST.db')
    print ("Opened database successfully")

def closeDataBaseConnection():
    conn.close()
    
def addToDataBase(ordernumber, samples, tests, duedate):
    conn.execute("INSERT INTO QBENCHTEST (ORDERNUMBER,SAMPLES,TESTS,DUEDATE, ONTRELLO) \
          VALUES (?, ?, ?, ?, 0)", (ordernumber, samples, tests, duedate));
    conn.commit()
    
def displayDataBase():
    cursor = conn.execute("SELECT id, ordernumber, samples, tests, duedate, ontrello from QBENCHTEST")
    '''for row in cursor:
       print ("ID = ", row[0])
       print ("ORDER = ", row[1])
       print ("SAMPLES = ", row[2])
       print ("TESTS = ", row[3])
       print ("DUEDATE = ", row[4])
       print ("ONTRELLO", row[5], "\n")
    print ("Operation done successfully")'''
    return cursor

def unitTest():
    addToDataBase("&&&&&&&&&", "1939393|939393|2393993|DJHADHF", "Moisture|Mycotoxins|Heavy Metals", "11/01/2018")



#unitTest()
#displayDataBase()
#closeDataBaseConnection()

#conn.close()
