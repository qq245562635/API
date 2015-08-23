import numpy as np
import pandas as pd
import MySQLdb as mdb

initialCash = 100000.0
initialEquity = 0.0

hostName = 'localhost'
userName = 'sec_user'
passWord = 'password'
dataBase = 'securities_master'

def fetchDataFromDB(symbol,beginDate,endDate):
    db = mdb.connect(hostName,userName,passWord,dataBase)
    cursor = db.cursor()
    retrieveCommond = "select * from dailyStockMarket where Symbol = '%s'and priceDate >= '%s'and priceDate <= '%s'"%(symbol,beginDate,endDate)
    cursor.execute(retrieveCommond)
    results = cursor.fetchall()
    resList = []
    for item in results:
        resList.append(item)
    dataDF = pd.DataFrame(resList)
    dataDF.columns = ['ID','Symbol','priceDate', 'openPrice', 'highPrice', 'lowPrice', 'closePrice', 'adjClosePrice','Volume']
    dataDF.index = dataDF.priceDate
    del dataDF['ID']
    del dataDF['Symbol']
    del dataDF['priceDate']
    return dataDF
    db.close()

def fetchPortfolioData(stockList, beginDate, endDate):
