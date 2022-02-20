import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic("matplotlib", " inline")
import seaborn as sns
sns.set()


madrid_2001 = pd.read_csv("C:/madrid_2001.csv")
madrid_2001.head()


madrid_2001.dropna().describe()


plt.figure(figsize=(20, 20))
sns.heatmap(madrid_2001.corr(), annot=True, fmt=" .2f");


madrid_2002 = pd.read_csv("C:/madrid_2002.csv")
madrid_2002.head()


madrid_2002.dropna().describe()


plt.figure(figsize=(20, 20))
sns.heatmap(madrid_2002.corr(), annot=True, fmt=" .2f");


madrid_2003 = pd.read_csv("C:/madrid_2003.csv")
madrid_2003.head()


madrid_2003.dropna().describe()


plt.figure(figsize=(20, 20))
sns.heatmap(madrid_2003.corr(), annot=True, fmt=" .2f");


madrid_2004 = pd.read_csv("C:/madrid_2004.csv")
madrid_2004.head()


madrid_2004.dropna().describe()


plt.figure(figsize=(20, 20))
sns.heatmap(madrid_2004.corr(), annot=True, fmt=" .2f");


madrid_2005 = pd.read_csv("C:/madrid_2005.csv")
madrid_2005.head()


madrid_2005.dropna().describe()


plt.figure(figsize=(20, 20))
sns.heatmap(madrid_2005.corr(), annot=True, fmt=" .2f");


madrid_2006 = pd.read_csv("C:/madrid_2006.csv")
madrid_2006.head()


madrid_2006.dropna().describe()


plt.figure(figsize=(20, 20))
sns.heatmap(madrid_2006.corr(), annot=True, fmt=" .2f");


madrid_2007 = pd.read_csv("C:/madrid_2007.csv")
madrid_2007.head()


madrid_2007.dropna().describe()


plt.figure(figsize=(20, 20))
sns.heatmap(madrid_2007.corr(), annot=True, fmt=" .2f");


madrid_2008 = pd.read_csv("C:/madrid_2008.csv")
madrid_2008.head()


madrid_2008.dropna().describe()


plt.figure(figsize=(20, 20))
sns.heatmap(madrid_2008.corr(), annot=True, fmt=" .2f");


madrid_2009 = pd.read_csv("C:/madrid_2009.csv")
madrid_2009.head()


madrid_2009.dropna().describe()


plt.figure(figsize=(20, 20))
sns.heatmap(madrid_2009.corr(), annot=True, fmt=" .2f");


madrid_2010 = pd.read_csv("C:/madrid_2010.csv")
madrid_2010.head()


madrid_2010.dropna().describe()


plt.figure(figsize=(20, 20))
sns.heatmap(madrid_2010.corr(), annot=True, fmt=" .2f");


madrid_2011 = pd.read_csv("C:/madrid_2011.csv")
madrid_2011.head()


madrid_2011.dropna().describe()


plt.figure(figsize=(20, 20))
sns.heatmap(madrid_2011.corr(), annot=True, fmt=" .2f");


madrid_2012 = pd.read_csv("C:/madrid_2012.csv")
madrid_2012.head()


madrid_2012.dropna().describe()


plt.figure(figsize=(20, 20))
sns.heatmap(madrid_2012.corr(), annot=True, fmt=" .2f");


madrid_2013 = pd.read_csv("C:/madrid_2013.csv")
madrid_2013.head()


madrid_2013.dropna().describe()


plt.figure(figsize=(20, 20))
sns.heatmap(madrid_2013.corr(), annot=True, fmt=" .2f");


madrid_2014 = pd.read_csv("C:/madrid_2014.csv")
madrid_2014.head()


madrid_2014.dropna().describe()


plt.figure(figsize=(20, 20))
sns.heatmap(madrid_2014.corr(), annot=True, fmt=" .2f");


madrid_2015 = pd.read_csv("C:/madrid_2015.csv")
madrid_2015.head()


madrid_2015.dropna().describe()


plt.figure(figsize=(20, 20))
sns.heatmap(madrid_2015.corr(), annot=True, fmt=" .2f");


madrid_2016 = pd.read_csv("C:/madrid_2016.csv")
madrid_2016.head()


madrid_2016.dropna().describe()


plt.figure(figsize=(20, 20))
sns.heatmap(madrid_2016.corr(), annot=True, fmt=" .2f");


madrid_2017 = pd.read_csv("C:/madrid_2017.csv")
madrid_2017.head()


madrid_2017.dropna().describe()


plt.figure(figsize=(20, 20))
sns.heatmap(madrid_2017.corr(), annot=True, fmt=" .2f");


madrid_2018 = pd.read_csv("C:/madrid_2018.csv")
madrid_2018.head()


madrid_2018.dropna().describe()


plt.figure(figsize=(20, 20))
sns.heatmap(madrid_2018.corr(), annot=True, fmt=" .2f");


madrid_stations = pd.read_csv("C:/stations.csv")
madrid_stations.head()


madrid_stations.dropna().describe()
