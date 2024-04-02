from pandas import *
import matplotlib.pyplot as plt

ROE_median = []
data_median = read_csv("C:/Users/Charles Lee/OneDrive - CUHK-Shenzhen/FIN3080_2/problem3_ans.csv")
for i in data_median['ROEC']:
    ROE_median.append(i)
data = read_csv("C:/Users/Charles Lee/OneDrive - CUHK-Shenzhen/FIN3080_2/problem3_data.csv")
data_1 = data
percent_list = []
for i in range(2011, 2021):
    data_2011 = data_1[data_1['EndDate'] == f'{i}-12-31']
    data_2011_company = data_2011[data_2011['ROEC'] >= ROE_median[i-2011]]
    data_1 = data_1[data_1['Symbol'].isin(data_2011_company['Symbol'])]
    percent_list.append(data_2011_company.shape[0]/2363)


data_2 = data
growth_median = []
for i in data_median['growth rate']:
    growth_median.append(i)

percent_list_2 = []
for i in range(2011, 2021):
    data_2011 = data_2[data_2['EndDate'] == f'{i}-12-31']
    data_2011_company = data_2011[data_2011['RevenueGrowthRate'] >= growth_median[i-2011]]
    data_2 = data_2[data_2['Symbol'].isin(data_2011_company['Symbol'])]
    percent_list_2.append(data_2011_company.shape[0]/2363)

year_list = []
for i in range(2011, 2021):
    year_list.append(i)
percent_list[0] = 0.5
percent_list_2[0] = 0.5


plt.figure(figsize=(16, 8))
plt.plot(year_list, percent_list, color="#6950a1")
plt.plot(year_list, percent_list_2, color="#ef5b9c")
plt.xticks(year_list)
plt.xlabel('Year')
plt.ylabel('percentage')
plt.grid(True)
plt.title('percentage of continuous above median')
plt.legend(labels=['ROE', 'Growth rate'], loc='best')
plt.show()



