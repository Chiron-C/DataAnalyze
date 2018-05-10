# -*- coding:utf-8 -*-
import sys
import numpy as np
import pandas as pd
import seaborn as sns
from hmmlearn.hmm import GaussianHMM
from matplotlib import pyplot as plt
import tushare as tu
import seaborn as sns

n = 6  # 六个隐藏状态
beginTime = '2015-1-1'
endTime = '2018-12-1'
data = tu.get_hist_data('sh', beginTime, endTime,'D')
high = data['high']
low = data['low']

volume = data['volume']
close = data['close'][5:]
Date = pd.to_datetime(data.index[5:])
print(Date)
logDel = (np.log(np.array(high)) - np.log(np.array(low)))[5:]
logRet1 = np.array(np.diff(np.log(close)))[5:]
logRet5 = np.log(np.array(close[5:])) - np.log(np.array(close[:-5]))  # 指數對數收益差
logVol5 = np.log(np.array(volume[5:])) - np.log(np.array(volume[:-5]))  # 指數對數交易量差
plt.hist(logVol5,200,normed=1,facecolor='green',alpha=0.75)
# plt.show()
# print(logDel)
A = np.column_stack([logDel[:100], logRet5[:100], logVol5[:100]])#1D-2D
print(A)
model = GaussianHMM(n_components=6, covariance_type='diag', n_iter=2000).fit(A)
hidden_states = model.predict(A)
print(hidden_states)
plt.figure(figsize=(10, 5))
sns.set_style('white')
for i in range(model.n_components):
        pos = (hidden_states==i)
        plt.plot(Date[i], close[i], 'o', label='hidden state %d' % i, lw=360)
        plt.legend()
        plt.grid(10)
plt.show()

