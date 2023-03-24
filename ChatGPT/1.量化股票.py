

import pandas as pd
import numpy as np
"""以下是一个简单的python量化算法，用于计算股票收益："""

# 导入必要的库

# 读取股票数据
data = pd.read_csv('stock_data.csv')

# 初始化变量
cash = 100000  # 初始资金
shares = 0  # 初始股票份数

# 计算收益
for row in data.iterrows():
    price = row[1]['price']  # 获取当前价格
    if cash > price:  # 如果现金够买
        shares += 1  # 买入一份股票
        cash -= price  # 扣除购买费用
    elif shares > 0:  # 如果持有股票
        cash += price  # 卖出股票
        shares -= 1  # 减少持有份数

# 计算收益率
earnings = cash + shares * data.iloc[-1]['price']  # 计算总资产
returns = (earnings - 100000) / 100000  # 计算收益率

print('总资产：', earnings)
print('收益率：', returns)
