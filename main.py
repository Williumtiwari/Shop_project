import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv(
    'data.csv',
    parse_dates=['Date'])
    

# z = data.head(9)
# print(z)
# x = data.shape
# print(x)
# data.info()
# data.describe()
# data['Unit_Cost'].describe()
# data['Unit_Cost'].mean()
# data['Unit_Cost'].median()
#data['Unit_Cost'].plot(kind='box', vert=False, figsize=(14,6))
data['Unit_Cost'].plot(kind='density', figsize=(14,6))
# ax = data['Unit_Cost'].plot(kind='density', figsize=(14,6)) # kde
# ax.axvline(data['Unit_Cost'].mean(), color='red')
# ax.axvline(data['Unit_Cost'].median(), color='green')
# ax = data['Unit_Cost'].plot(kind='hist', figsize=(14,6))
# ax.set_ylabel('Number of Sales')
# ax.set_xlabel('dollars')
