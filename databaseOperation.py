__author__ = 'Conan'
#!/usr/bin/python

import pandas as pd
import urllib2
import MySQLdb as mdb
import datetime as dt
import matplotlib.pyplot as plt

symbol = ['AMZN','AAPL','GOOG']
beginDate = dt.date(2015,6,1)
endDate = dt.date(2015,6,30)

def loadDataIntoDB(symbol = None, beginDate=None, endDate = None):
    hostName = 'localhost'
    userName = 'sec_user'
    passWord = 'password'
    dataBase = 'securities_master'
    db = mdb.connect(hostName,userName,passWord,dataBase)
    cursor = db.cursor()
    yahoo_url = "http://ichart.finance.yahoo.com/table.csv?s=%s&a=%s&b=%s&c=%s&d=%s&e=%s&f=%s"%(symbol,beginDate.month-1,beginDate.day,beginDate.year,endDate.month-1,endDate.day,endDate.year )
    yf_data = urllib2.urlopen(yahoo_url).readlines()[1:]
    for data in yf_data:
        cdata = data.split(',')
        insertCommond = "INSERT INTO dailyStockMarket(Symbol, priceDate, openPrice, highPrice, lowPrice, closePrice, adjClosePrice, Volume) VALUES ('%s', '%s', '%s', '%s', '%s', '%s','%s','%s')"%(symbol,cdata[0],cdata[1],float(cdata[2]),float(cdata[3]),float(cdata[4]),float(cdata[6]),int(cdata[5]))
        cursor.execute(insertCommond)
        db.commit()
    db.close()

def fetchDataFromDB(symbol,beginDate,endDate):
    hostName = 'localhost'
    userName = 'sec_user'
    passWord = 'password'
    dataBase = 'securities_master'
    db = mdb.connect(hostName,userName,passWord,dataBase)
    cursor = db.cursor()
    retrieveCommond = "select * from dailyStockMarket where Symbol = '%s'and priceDate >= '%s'and priceDate <= '%s'"%(symbol,beginDate,endDate)
    cursor.execute(retrieveCommond)
    results = cursor.fetchall()
    return results
    db.close()

for sym in symbol:
    loadDataIntoDB(sym,beginDate,endDate)
'''
res = fetchDataFromDB("GOOG",beginDate,endDate)
resl =[]
for item in res:
    resl.append(item)
dfres = pd.DataFrame(resl)
dfres.columns = ['ID','Symbol','priceDate', 'openPrice', 'highPrice', 'lowPrice', 'closePrice', 'adjClosePrice','Volume']
dfres.index = dfres.priceDate
del dfres['ID']
del dfres['Symbol']
del dfres['priceDate']
print dfres
'''
'''
pType = 'adjClosePrice'
price = dfres[pType]
date = dt.date(2015,6,2)
print price[date]
print "..."
price = dfres.adjClosePrice
if 560 > 530.0:
    print price.index.values
    print "..."
'''
