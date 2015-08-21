dict = {'AAPL': 100, 'GOOG': 200}
'''
for item in dict.items():
    print item[0]
'''

if 'GOOG' in dict:
    del dict['AAPL']

else:
    print "YES"
print dict