
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
print sys.path[0]
import pandas as pd
path = sys.path[0] + '/GOOG.csv'
data = pd.read_csv(path)
print data.loc[1,'priceDate']
'''
import datetime as dt
a = dt.date(2015,5,1)
b = dt.date(2015,5,2)
c = a-b

print int(c.days)
'''