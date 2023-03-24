import time
path = 'DataAnalysis/Pandas/Test_Case.xlsx'

"""
安装 
pip install pandas 
pip install openpyxl 
"""

# 1.导入pandas模块
import pandas as pd

# 2.把Excel文件中的数据读入pandas
df = pd.read_excel(path)
print(df)
# 3.读取excel的某一个sheet
df = pd.read_excel(path, sheet_name='login')
print(df)
# 4.获取列标题
print(df.columns)
# 5.获取列行标题
print(df.index)
# 6.制定打印某一列
print(df["url"])
# 7.描述数据
print(df.describe())


t1 = time.time()
for indexs in df.index:
    print(df.loc[indexs].values[0:-1])
t2 = time.time()
print("使用pandas工具包遍历12000行数据耗时：%.2f 秒"%(t2-t1))
