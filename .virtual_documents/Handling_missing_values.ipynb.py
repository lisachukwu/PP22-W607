#important library
import pandas as pd
import glob
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# loading all csv file names
files = glob.glob("csvs_per_year/*.csv")
# reading csv files
for index,file in enumerate(files):
    files[index] = pd.read_csv(file,index_col='date',parse_dates=['date'])
# merging all csv files
df = pd.concat(files)
df.info()


df.shape


df.head()


df.tail()


descr= df.describe()
descr.loc()


#summing up missing values in the data set and saving it in 'missing_count'
df.isnull().sum().sort_values()
missing_count_df = pd.DataFrame(missing_count, columns=['missing_values'])
missing_count_df


#Presenting percentage of data points, missing in each feature
string_percentage = []
float_percentage =[]
for key,value in missing_count.items():
    percent_missing = (value/3808224)*100
    float_percentage.append(percent_missing)
    string_percentage.append(str(percent_missing)+'get_ipython().run_line_magic("')", "")
missing_df = pd.DataFrame(index = missing_count.keys(), columns=['Percentage_missing'])
missing_df['Percentage_missing']= string_percentage
missing_df


#Plotting the amount of missing data points in the dataset
plt.style.use('fivethirtyeight')
missing_count_df.plot(kind='bar',figsize=(15,8))


#filling missing data with closest data point after 
df_ffill = df.fillna(method='ffill')
#filling missing data with closest data point before
df_bfill = df.fillna(method='bfill')


df_ffill.isnull().sum()


df_bfill.isnull().sum()


df_drop= df.dropna()
df_drop.shape


#Removing features with more than 72% NAN entries
df_copy = df.copy()
missing_dict = dict(zip(missing_count.keys(),float_percentage))
for key,value in missing_dict.items():
    if value > 72:
        df_copy.drop(key,inplace=True, axis= 1)
df_copy.shape


df.head()


df_copy.head()


df_copy_missing_dict = df_copy.isnull().sum()
df_copy_missing_dict


df_copy_missing_dict.keys()


#Replacing missing data in each column with the feature's median value and storing in a new variable 'clean_df'
clean_df = df_copy.copy()
for feature in df_copy_missing_dict.keys():
    clean_df[feature].fillna(clean_df[feature].median(),inplace=True)
clean_df.head()


#Checking to confirm if missing values have been addressed
clean_df.isnull().sum()
