#important library
import pandas as pd
import glob
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic("matplotlib", " inline ")


# loading all csv file names
files = glob.glob("csvs_per_year/*.csv")


# reading csv files
for index,file in enumerate(files):
    files[index] = pd.read_csv(file,index_col='date',parse_dates=['date'])


# merging all csv files
df = pd.concat(files)


df.info()


df.head()


#cunt of data is null
df.isnull().sum().sort_values()


#percentage of data is null
null_precentage = round((df.isnull().sum() * 100) / 3808224 , 2).sort_values()
null_precentage


#dataset with less then 50% null count
imp_index = null_precentage[null_precentage < 50].index.to_list()
clean_df = df[imp_index]
pd.options.mode.chained_assignment = None  # default='warn'


# # replacing nan with median values
# clean_df = clean_df.transform(lambda x: x.fillna(x.median()))


# replacing nan values with respect to city
clean_df.iloc[:,1:-1] = clean_df.groupby('station').transform(lambda x:x.fillna(x.median()))
clean_df['month'] = clean_df.index.month

# replacing leftover nan values with respect to month
clean_df.iloc[:,0:-2] = clean_df.groupby('month').transform(lambda x:x.fillna(x.mean()))
clean_df = clean_df.drop('month',axis=1)


clean_df.head()


clean_df.describe()


clean_df.info()


clean_df.tail()


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


sns.lineplot(x=clean_df.index.year,y=clean_df["AQI_calculated"])
