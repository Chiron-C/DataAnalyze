import tushare as ts
import datetime
import sys
from Pretreatment import getDict as d
# print()
sys.path.append('F:\DataAnalyze\HMM\Pretreatment.py')
hist=ts.get_hist_data('600847',start='2014-1-1',end='2015-5-7')
# for i in hist['close']:
#     print(i)
# for i in hist['volume']:
#     print(i)
pre=d()
print(pre.get('close'))
#print(ts.get_today_all()['code'])
#print(ts.get_tick_data('600848',date='2014-1-1').head(10))
# print(ts.get_realtime_quotes('000581'))
# print(ts.get_today_ticks('000581'))
# print(ts.get_index())
# print(ts.realtime_boxoffice())
# print(datetime.datetime(2010,1,1).strftime('%Y-%m-%d'))