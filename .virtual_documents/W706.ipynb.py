#important library
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.options.mode.chained_assignment = None  # default='warn'


# loading all csv file names
files = glob.glob("csvs_per_year/*.csv")
# reading csv files
for index,file in enumerate(files):
    files[index] = pd.read_csv(file,index_col='date',parse_dates=['date'])
# merging all csv files
df = pd.concat(files)


df.head()


df.tail()


df.info()


df.describe()


#cunt of data is null
df.isnull().sum().sort_values()


#percentage of data is null
null_precentage = round((df.isnull().sum() * 100) / 3808224 , 2).sort_values()
null_precentage


#visualization of null datas
sns.heatmap(df.isnull(),yticklabels=False)


#dataset with less then 50% null count
imp_index = null_precentage[null_precentage < 50].index.to_list()
df1 = df[imp_index]
df1['month'] = df.index.month


#percentage of data is null
round((df1.isnull().sum() * 100) / 3808224 , 2).sort_values()


# replacing nan values with respect to city
df1.iloc[:,1:] = df1.groupby('station').transform(lambda x:x.fillna(x.mean()))
sns.heatmap(df1.isnull(),yticklabels=False,cbar=False,cmap='viridis')


# replacing nan values with respect to month
df1.iloc[:,:-1] = df1.groupby('month').transform(lambda x:x.fillna(x.mean()))
sns.heatmap(df1.isnull(),yticklabels=False,cbar=False,cmap='viridis')


df1.head()
