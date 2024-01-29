import numpy as np
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.offline import download_plotlyjs, init_notebook_mode, iplot

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

data = pd.read_csv('breadbasket.csv')

# 印出前五行
print("1、Dataset\n", data.head())

# 增加新列quantity，並將所有值設為1
data['Quantity'] = 1

# 印出data的行、列、總數、交易筆數
print("\n2、Characteristic of Dataset") 
print("Database dimension :", data.shape)
print("Database size      :", data.size)
print("Transaction amount :", data['Transaction'].nunique())

# 顯示data type為object的描述
print("\n3、Description of Dataset") 
print(data.describe(include=object))

# 每項商品銷售數量的長條圖
itemFrequency = data['Item'].value_counts().sort_values(ascending=False)
fig = px.bar(itemFrequency.head(20), title='20 Most Frequent Items', color=itemFrequency.head(20), color_continuous_scale=px.colors.sequential.Mint)
fig.update_layout(margin=dict(t=50, b=0, l=0, r=0), titlefont=dict(size=20), xaxis_tickangle=-45, plot_bgcolor='white', coloraxis_showscale=False)
fig.update_yaxes(showticklabels=False, title=' ')
fig.update_xaxes(title=' ')
fig.update_traces(texttemplate='%{y}', textposition='outside', hovertemplate = '<b>%{x}</b><br>No. of Transactions: %{y}')
fig.show()

# 處理資料空缺及空格
data['Item'] = data['Item'].str.strip()
data.dropna(axis = 0, subset = ['Transaction'], inplace = True)
data['Transaction'] = data['Transaction'].astype('str')

# 將data轉成每一行為一筆交易，當每項商品成為一列，1表示該筆交易有消費該商品，0則相反
basket = (data[data['weekday_weekend'] =="weekend"]
          .groupby(['Transaction', 'Item'])['Quantity']
          .sum().unstack().reset_index().fillna(0)
          .set_index('Transaction'))

# define hot_encode函數。如果數量<=0，則返回0；如果數量>=1，則返回1
def hot_encode(x):
    if(x<= 0):
        return 0
    if(x>= 1):
        return 1
  
basket_encoded = basket.applymap(hot_encode)
basket = basket_encoded

# 建構模型
frequent_items = apriori(basket, min_support = 0.02, use_colnames = True)

# 生成關聯規則
rules = association_rules(frequent_items, metric ="lift", min_threshold = 1)
rules = rules.sort_values(['confidence', 'lift'], ascending =[False, False])
print("\n4、Association rules") 
print(rules.head())