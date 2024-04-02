from pandas import *


data = read_csv("C:/Users/Charles Lee/OneDrive - CUHK-Shenzhen/FIN3080_2/problem3_data.csv")
data['growth rate'] = data['TotalRevenue'].pct_change() * 100
data = data[data['EndDate'] >= '2011-05-01']
median_ROE = data.groupby('EndDate')['ROEC'].median()
median_growth_rate = data.groupby('EndDate')['growth rate'].median()
median_ROE.to_csv("C:/Users/Charles Lee/OneDrive - CUHK-Shenzhen/FIN3080_2/median_ROE.csv")
median_growth_rate.to_csv("C:/Users/Charles Lee/OneDrive - CUHK-Shenzhen/FIN3080_2/median_growth.csv")

data_ROE = read_csv("C:/Users/Charles Lee/OneDrive - CUHK-Shenzhen/FIN3080_2/median_ROE.csv")
data_growth = read_csv("C:/Users/Charles Lee/OneDrive - CUHK-Shenzhen/FIN3080_2/median_growth.csv")
data_ans = data_ROE.merge(data_growth, left_on="EndDate", right_on="EndDate", how="left")
data_ans = data_ans[data_ans["EndDate"] >= '2011-12-01']
data_ans.to_csv("C:/Users/Charles Lee/OneDrive - CUHK-Shenzhen/FIN3080_2/problem3_ans.csv", index=False)

data = read_csv('C:/Users/Charles Lee/OneDrive - CUHK-Shenzhen/FIN3080_2/problem3_data.csv')
data['RevenueGrowthRate'] = (data['TotalRevenue'] - data['TotalRevenue'].shift(1)) / data['TotalRevenue'].shift(1) * 100
data.to_csv('C:/Users/Charles Lee/OneDrive - CUHK-Shenzhen/FIN3080_2/problem3_data.csv',index=False)


