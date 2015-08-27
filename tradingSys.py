
import numpy as np
import pandas as pd
import MySQLdb as mdb
import sys
import datetime as dt

class tradingSys(object):
    initialCash = 100000.0
    initialEquity = 0.0
    portfolio = {}
    def __init__(self):
        self.cash = self.initialCash
        self.equity = self.initialEquity

    beginDate = dt.date(2015,6,1)
    endDate = dt.date(2015,6,30)

    def fetchDataFromDB(self,symbol,beginDate,endDate):
        hostName = 'localhost'
        userName = 'sec_user'
        passWord = 'password'
        dataBase = 'securities_master'
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
        path = sys.path[0]+'/'+symbol+'.csv'
        dataDF.to_csv(path)

    def fetchPortfolioData(self, stockList, beginDate, endDate):
        for stock in stockList:
            portfolioData[stock] = fetchDataFromDB(stock,beginDate,endDate)

    def order(self, stock, shares,date,priceType):
        path = sys.path[0] + '/'+stock+'.csv'
        priceData = pd.read_csv(path)
        for index in range(len(priceData)):
            priceData.priceDate[index] = dt.datetime.strptime(priceData.priceDate[index],"%Y-%m-%d")
        priceData.index = priceData.priceDate
        price = priceData.loc[date,priceType]
        self.cash = self.cash - price * shares
        self.equity = self.equity + price * shares
        self.portfolio['CASH'] = self.cash
        self.portfolio[stock] = shares


<<<<<<< HEAD


=======
mytradingSys = tradingSys()
beginDate = dt.date(2015,6,1)
endDate = dt.date(2015,6,30)
#mytradingSys.fetchDataFromDB('GOOG',beginDate,endDate)
mytradingSys.order('GOOG',20,beginDate,'adjClosePrice')
print mytradingSys.portfolio
>>>>>>> origin/master
