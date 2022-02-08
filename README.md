"# W607---rnn-HAMOYE" 
import pandas as pd
import glob 
import os
#merging all the csv files
filesjoined = os.path.join(r"C:\Users\TENECE\Desktop\csv\csvs_per_year\csvs_per_year", "madrid*.csv")
new_file = glob.glob(filesjoined)
merged = pd.concat(map(pd.read_csv, new_file), ignore_index = True)
print(merged)
merged.describe() #describing the merged files
#merged.isnull().sum() #checking for null values
