#important library
import pandas as pd
import glob


# loading all csv file names
files = glob.glob("csvs_per_year/*.csv")


# reading csv files
for index,file in enumerate(files):
    files[index] = pd.read_csv(file,index_col='date',parse_dates=['date'])


# merging all csv files
df = pd.concat(files)


df.info()


df.head()



