import pandas as pd
import glob
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


station_df = pd.read_csv('stations.csv')


station_df.head()


station_df.info()


sns.countplot(x = station_df['elevation'])


sns.boxplot(x = station_df['lat'])


sns.boxplot(x = station_df['lon'])


plt.scatter(station_df['lat'], station_df['elevation'])


plt.scatter(station_df['lon'], station_df['elevation'])
