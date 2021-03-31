#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd

stock_dividend_path = 'fy-stock-dividend.csv'
profit_loss_path = 'fy-profit-and-loss.csv'
blance_path = 'fy-balance-sheet.csv'
dividend_record_path = '国内株配当実績取得ツール_20200513.xlsm'
target_path = 'fy-merged-sheet.csv'

blance_data_frame = pd.read_csv(blance_path,header=1,usecols=['コード','年度','自己資本比率'])
profit_data_frame = pd.read_csv(profit_loss_path,header=1,usecols=['コード','売上高','営業利益'])
stock_data_frame = pd.read_csv(stock_dividend_path,header=1,usecols=['コード','一株配当','配当性向'])
dividend_record_data_frame = pd.read_excel(dividend_record_path,header=1,usecols=['コード','連続増配','減配なし'])

data_list = [blance_data_frame, profit_data_frame, stock_data_frame, dividend_record_data_frame]

tmp = data_list[0]
for data in data_list[1:]:
    tmp = pd.merge(tmp,data,on='コード')
tmp.to_csv(target_path,index=False,encoding='shift-jis')


# In[9]:


jupyter nbconvert --to python make_csv_list.ipynb


# In[ ]:




