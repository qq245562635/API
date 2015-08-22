###################################
# Created by Conan on July 26     #
# To get a stock price (O,H,L,C,V)#
###################################

import pandas as pd
import numpy as np
import urllib2
import datetime as dt
import matplotlib.pyplot as plt

###################################
# symbol: the stock ticker        #
# interval: time interval(seconds)#
# period: time period (days)      #
###################################

def get_google_data(symbol, interval, period):
    url = 'http://www.google.com/finance/getprices?i='
    url += str(interval) + '&p=' + str(period)
    url += 'd&f=d,o,h,l,c,v&df=cpct&q=' + symbol
    response = urllib2.urlopen(url)
    data = response.read().split('\n')
    #actual data starts at index = 7 for American stocks
    #first line contains full timestamp,
    #every other line is offset of period from timestamp
    parsed_data = [] # store the parsed data
    anchor_stamp = ''
    end = len(data)
    coef = np.array(range(390*60/interval))+1
    truets = []
    for i in range(7, end):
        cdata = data[i].split(',')
        if 'a' in cdata[0]:
            #first one record anchor timestamp
            anchor_stamp = cdata[0].replace('a', '')
            cts = int(anchor_stamp)
	    truets.append(int(anchor_stamp)+(coef*interval))
        else:
            try:
                coffset = int(cdata[0])
                cts = int(anchor_stamp) + (coffset * interval)
                parsed_data.append((dt.datetime.fromtimestamp(float(cts)), float(cdata[1]), float(cdata[2]), float(cdata[3]), float(cdata[4]), float(cdata[5])))
            except:
                pass # for time zone offsets thrown into data
    df = pd.DataFrame(parsed_data)
    df.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
    df.index = df.Time
    del df['Time']
    return df

if __name__=="__main__":
    spy = get_google_data("AAPL",300,3)
    print spy['Close']
