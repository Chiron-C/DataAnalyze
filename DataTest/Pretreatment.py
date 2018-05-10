import tushare as tu
import datetime
def getDict():
    strFomat='%Y-%m-%d'
    start_date = datetime.datetime(2010,1,1).strftime(strFomat)
    end_date =datetime.datetime(2018,1,1).strftime(strFomat)
    Tvalue = tu.get_hist_data('600848',start_date,end_date)
    close=[]
    high=[]
    low=[]
    volume=[]
    dict={}
    for i in Tvalue['close']:
        close.append(i)
    for i in Tvalue['high']:
        high.append(i)
    for  i in Tvalue['low']:
        low.append(i)
    for i in Tvalue['volume']:
        volume.append(i)
    dict['close']=close
    dict['high']=high
    dict['low']=low
    dict['volume']=volume
    return dict
