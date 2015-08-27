
#dict = {'AAPL': 100, 'GOOG': 200}
'''
for item in dict.items():
    print item[0]
'''
'''
if 'GOOG' in dict:
    del dict['AAPL']

else:
    print "YES"
print dict
'''

import sys
import datetime as dt
#print sys.path[0]
import pandas as pd
path = sys.path[0] + '/GOOG.csv'
data = pd.read_csv(path)
a = []
for index in range(len(data)):
    #a = data.priceDate[index]
    a.append(dt.datetime.strptime(data.priceDate[index], "%Y-%m-%d"))

data.index = a
print data.index.values[0]

del data['priceDate']
#dt = dt.datetime.strptime(, "%Y-%m-%d)
'''
import datetime as dt
a = dt.date(2015,5,1)
b = dt.date(2015,5,2)
c = a-b

print int(c.days)
'''