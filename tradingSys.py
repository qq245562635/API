
import numpy as np
import pandas as pd
import MySQLdb as mdb

class portfolio(object):
    initialCash = 100000.0
    initialEquity = 0.0

    cash = initialCash
equity = initialEquity
portfolio = {}

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
    db.close()
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

def fetchPortfolioData(stockList, beginDate, endDate):
    portfolioData = {}
    for stock in stockList:
        portfolioData[stock] = fetchDataFromDB(stock,beginDate,endDate)
    return portfolioData

def order(stock, shares, price):
    cash = cash - price * shares
    equity = price * shares
    shares = shares;



