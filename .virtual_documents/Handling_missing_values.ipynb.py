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
descr


#summing up missing values in the data set and saving it in 'missing_count'
missing_count = df.isnull().sum()
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


clean_df["PM10_24hr_avg"] = clean_df.groupby("station")["PM10"].rolling(window = 24, min_periods = 1).mean().values
clean_df["SO2_24hr_avg"] = clean_df.groupby("station")["SO_2"].rolling(window = 24, min_periods = 1).mean().values
clean_df["NOx_24hr_avg"] = clean_df.groupby("station")["NOx"].rolling(window = 24, min_periods = 1).mean().values
clean_df["CO_8hr_max"] = clean_df.groupby("station")["CO"].rolling(window = 8, min_periods = 1).max().values
clean_df["O3_8hr_max"] = clean_df.groupby("station")["O_3"].rolling(window = 8, min_periods = 1).max().values


## PM10 Sub-Index calculation
def get_PM10_subindex(x):
    if x <= 50:
        return x
    elif x <= 100:
        return x
    elif x <= 250:
        return 100 + (x - 100) * 100 / 150
    elif x <= 350:
        return 200 + (x - 250)
    elif x <= 430:
        return 300 + (x - 350) * 100 / 80
    elif x > 430:
        return 400 + (x - 430) * 100 / 80
    else:
        return 0

clean_df["PM10_SubIndex"] = clean_df["PM10_24hr_avg"].apply(lambda x: get_PM10_subindex(x))


## SO2 Sub-Index calculation
def get_SO2_subindex(x):
    if x <= 40:
        return x * 50 / 40
    elif x <= 80:
        return 50 + (x - 40) * 50 / 40
    elif x <= 380:
        return 100 + (x - 80) * 100 / 300
    elif x <= 800:
        return 200 + (x - 380) * 100 / 420
    elif x <= 1600:
        return 300 + (x - 800) * 100 / 800
    elif x > 1600:
        return 400 + (x - 1600) * 100 / 800
    else:
        return 0

clean_df["SO2_SubIndex"] = clean_df["SO2_24hr_avg"].apply(lambda x: get_SO2_subindex(x))


## NOx Sub-Index calculation
def get_NOx_subindex(x):
    if x <= 40:
        return x * 50 / 40
    elif x <= 80:
        return 50 + (x - 40) * 50 / 40
    elif x <= 180:
        return 100 + (x - 80) * 100 / 100
    elif x <= 280:
        return 200 + (x - 180) * 100 / 100
    elif x <= 400:
        return 300 + (x - 280) * 100 / 120
    elif x > 400:
        return 400 + (x - 400) * 100 / 120
    else:
        return 0

clean_df["NOx_SubIndex"] = clean_df["NOx_24hr_avg"].apply(lambda x: get_NOx_subindex(x))


## CO Sub-Index calculation
def get_CO_subindex(x):
    if x <= 1:
        return x * 50 / 1
    elif x <= 2:
        return 50 + (x - 1) * 50 / 1
    elif x <= 10:
        return 100 + (x - 2) * 100 / 8
    elif x <= 17:
        return 200 + (x - 10) * 100 / 7
    elif x <= 34:
        return 300 + (x - 17) * 100 / 17
    elif x > 34:
        return 400 + (x - 34) * 100 / 17
    else:
        return 0

clean_df["CO_SubIndex"] = clean_df["CO_8hr_max"].apply(lambda x: get_CO_subindex(x))


## O3 Sub-Index calculation
def get_O3_subindex(x):
    if x <= 50:
        return x * 50 / 50
    elif x <= 100:
        return 50 + (x - 50) * 50 / 50
    elif x <= 168:
        return 100 + (x - 100) * 100 / 68
    elif x <= 208:
        return 200 + (x - 168) * 100 / 40
    elif x <= 748:
        return 300 + (x - 208) * 100 / 539
    elif x > 748:
        return 400 + (x - 400) * 100 / 539
    else:
        return 0

clean_df["O3_SubIndex"] = clean_df["O3_8hr_max"].apply(lambda x: get_O3_subindex(x))


clean_df.head()


clean_df["AQI_calculated"] = round(clean_df[["PM10_SubIndex","NOx_SubIndex", "CO_SubIndex", "O3_SubIndex"]].max(axis = 1))


clean_df["AQI_calculated"]


sns.lineplot(x=clean_df.index.year,y=clean_df["AQI_calculated"])
