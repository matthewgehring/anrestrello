import sqlite3
#Table Start
"""conn.execute('''CREATE TABLE QBENCHTEST
         (ID INTEGER PRIMARY KEY,
         ORDERNUMBER     TEXT    NOT NULL,
         SAMPLES         TEXT    NOT NULL,
         TESTS           TEXT    NOT NULL,
         ONTRELLO        INT     NOT NULL);''')"""

#print ("Table created successfully")

def connectToDataBase():
    conn = sqlite3.connect('qbenchTEST.db')
    print ("Opened database successfully")

def closeDataBaseConnection():
    conn.close()
def addToDataBase(ordernumber, samples, tests):
    conn.execute("INSERT INTO QBENCHTEST (ORDERNUMBER,SAMPLES,TESTS,ONTRELLO) \
          VALUES (?, ?, ?, 0)", (ordernumber, samples, tests));
    conn.commit()
    
def displayDataBase():
    cursor = conn.execute("SELECT id, ordernumber, samples, tests, ontrello from QBENCHTEST")
    for row in cursor:
       print ("ID = ", row[0])
       print ("ORDER = ", row[1])
       print ("SAMPLES = ", row[2])
       print ("TESTS = ", row[3])
       print ("ONTRELLO", row[4], "\n")
    print ("Operation done successfully")

def unitTest():
    addToDataBase("32423", "1939393|939393|2393993|DJHADHF", "Moisture|Mycotoxins|Heavy Metals")
