#-*- coding:utf-8-*-
import numpy as np
import tushare as tu
import datetime
from matplotlib import pyplot as pt
def create_date():
    timeFormat='%Y-%m-%d'
    startTime=datetime.datetime(2017,5,9).strftime(timeFormat)
    endTime=datetime.datetime(2018,5,9).strftime(timeFormat)
    data=tu.get_k_data('sh',startTime,endTime,'D')
    return data
def Exponential_Smooth(alpha,s):
    s2=np.zeros(s.shape)
    s2[0]=s[0]
    for i in range(1,len(s2)):#1是单指数
        s2[i]=alpha*s[i]+(1-alpha)*s2[i-1]
    return s2
def show_data(new_year,data,data_pre_d):
    date=data['date']
    close=data['close']
    pt.figure(figsize=(15,8),dpi=60)
    pt.plot(date,close,color='blue',label='actual value')
    pt.plot(new_year[3:],data_pre_d[2:],color='red',label='smooth value')
    pt.legend(loc='higher right')
    pt.title('Exponential Smooth')
    pt.xlabel('date')
    pt.ylabel('price')
    pt.xticks(date)
    pt.show()
def main():
    alpha=0.4
    pre_m=np.array(['2018-5-31','2018-6-30'])
    data=create_date()
    date=np.array(data['date'])
    close=np.array(data['close'])
    single_smooth=Exponential_Smooth(alpha,close)
    double_smooth=Exponential_Smooth(alpha,single_smooth)
    double_a=2*single_smooth-double_smooth
    double_b=(single_smooth-double_smooth)*(alpha/(1-alpha))
    s_pre_double=np.zeros(double_smooth.shape)
    for i in range(2,len(date)):
        s_pre_double[i]=double_a[i-1]+double_b[i-1]
    pre_next_m=double_a[-1]+double_b[-1]
    pre_next_t_m=double_a[-1]+2*double_b[-1]
    s_pre_double=np.insert(s_pre_double,len(s_pre_double),values=np.array(pre_next_m,pre_next_t_m),axis=0)
    new_m=np.insert(date,len(date),values=pre_m,axis=0)
    print(new_m)
    print(s_pre_double)
    print(data)
    show_data(new_m,data,s_pre_double)

if __name__=='__main__':
    main()