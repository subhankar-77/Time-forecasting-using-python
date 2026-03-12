import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from pandas import Series
#%matplotlib inline
import warnings
warnings.filterwarnings ("ignore")

train = pd.read_csv ("Train_SU63ISt.csv")
test = pd.read_csv("Test_0qrQsBZ.csv")

train_original = train.copy()
test_original = test.copy()


train['Datetime'] = pd.to_datetime(train.Datetime, format="%d-%m-%Y %H:%M")

test['Datetime'] = pd.to_datetime(train.Datetime, format="%d-%m-%Y %H:%M")

test_original['Datetime'] = pd.to_datetime(train.Datetime, format="%d-%m-%Y %H:%M")

train_original['Datetime'] = pd.to_datetime(train.Datetime, format="%d-%m-%Y %H:%M")

for i in (train, test, test_original, train_original):
    i['year']=i.Datetime.dt.year
    i['month']=i.Datetime.dt.month
    i['day']=i.Datetime.dt.date
    i['Hour']=i.Datetime.dt.hour

train['day of week'] = train['Datetime'].dt.dayofweek
temp = train ['Datetime']

def applyer(row):
    if row.dayofweek == 5 or row.dayofweek==6:
        return 1
    else:
        return 0
    
temp2=train['Datetime'].apply(applyer)
train['weekend']=temp2

train.index = train['Datetime']
df=train.drop(columns=['ID'])
ts = df['Count']
plt.figure(figsize=(16,8))
plt.plot(ts, label = "Passenger Count")
plt.title('Time Series')
plt.xlabel("Time(year-month)")
plt.ylabel("Passenger Count")
plt.legend(loc='best')

plt.show()

train.groupby('year')['Count'].mean.plot.bar()
train.groupby('month')['Count'].mean.plot.bar()

temp = train.grouby(['year', 'month'])['Count'].mean()
temp.plot(figsize=(15,5), title = 'Passenger Count(Monthwise)', fomtsize=14)

