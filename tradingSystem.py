import numpy as np
import pandas as pd
import MySQLdb as mdb
'''
def availableStockMarket():
    # Open database connection
    db = mdb.connect("localhost","sec_user", "password","securities_master")
    # Prepare a cursor object using cursor() method
    cursor = db.cursor()
'''

class Portfolio():
    cash = 100000.0
    equity = 0.0
    def __init__(self):
        self.stocks = {}
    def buyStock(self, stock_symbol, stock_amount):
        price = stockMarket.get_price(stock_symbol)
        if price * stock_amount < self.cash:
            self.stocks[stock_symbol] = stock_amount
        else:
            print "YOU DO NOT HAVE ENOUGH MONEY!"
    def sellStock(self, stock_symbol, stock_amount):
        price = stockMarket.get_price(stock_symbol)
        if stock_symbol in self.stocks:
            self.cash = self.cash + price * stock_amount
            updated_stock_amount = self.stocks[stock_symbol] - stock_amount
            if updated_stock_amount == 0:
                del self.stocks[stock_symbol]
            else:
                self.stocks[stock_symbol] = updated_stock_amount
        else:
            print "YOU HAVE NO POSITION IN THIS STOCK!"
'''
        def currentPortfolio(self):
            print 'The total cash is: ', self.cash
            print 'The stocks in your portfolio are: '
            for item in self.stocks.items():
                print item[0], ": ", item[1]
            return 0
'''
p = Portfolio()
p.