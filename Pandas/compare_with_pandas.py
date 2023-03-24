import pandas as pd
import polars as pl
import timeit

# 读取时间对比
start_df = timeit.default_timer()
df = pd.read_csv("/Users/lenskit/Desktop/aa.csv")
df = df.sort_values("company_name", ascending=False).head()
stop_df = timeit.default_timer()
print('time: ', stop_df - start_df)

start_pl = timeit.default_timer()
data = pl.read_csv("/Users/lenskit/Desktop/aa.csv")
data.sort(by="company_name", reverse=True).head()
stop_pl = timeit.default_timer()
print('time1: ', stop_pl - start_pl)

# 纵向拼接时间对比
start_df1 = timeit.default_timer()
df_1 = pd.read_csv('/Users/lenskit/Desktop/aa.csv')
df_2 = pd.read_csv('/Users/lenskit/Desktop/bb.csv')
df_1.append(df_2, ignore_index=True)
stop_df1 = timeit.default_timer()
print('time2: ', stop_df1 - start_df1)

start_pl1 = timeit.default_timer()
pl_1 = pl.read_csv('/Users/lenskit/Desktop/aa.csv')
pl_2 = pl.read_csv('/Users/lenskit/Desktop/bb.csv')
pl_1.vstack(pl_2)
stop_pl1 = timeit.default_timer()
print('time3: ', stop_pl1 - start_pl1)