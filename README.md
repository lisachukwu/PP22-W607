# Air Quality in Madrid (Different pollution levels in Madrid from 2001-2018)

This dataset is created out of the frustation of how inconvenient and irregular the historical data was provided in the Open Data website. It contains in a practical format 18 years (2001-2018) of hourly data in just a single file, which makes this dataset a great playground for time series analysis and other prediction tasks. How do different gases correlate their levels? Are there any changes in trends? Can they be mapped to the recent decisions made by the city council, or do they relate to rainy dates? What is the best model to predict pollution levels? How do the levels interpolate between the location of the stations? Are some gases more common at different elevations?

## Different files in the project are as follows:

### Handling_missing_values.ipynb 
Implements Exploratory Data Analysis, also handles missing data in the provided dataset. Strategy used in this file is: (1) Features with more than 72% missing data will be dropped. This is because the amount of known data points in these fearures is negligible compared to the amount of missing data. Imputing these values will lead to a huge bias in the data. (2) Missing values in other features will be replaced with their median values. This is to preserve the statistical property of each feature as much as possible. Median is used here instead of the mean because the mean can be affected by the presence of outliers.

### Project_Documentation.txt
Explains the different measurements present in the provided dataset. It also stated the different answers that we are able to obtain from our analysis.

### W706.ipynb
Contains the main file of the project. Its contents are : (1) Handling NaN Values (2) Removing unnecessary features (3) Exploring the Cleaned DataFrame (4) AQI Calculation (5) Visualization of Variables

### dataset_visualization.ipynb
Plots heatmaps based on the datasets provided with respect to different years.

### madrid.h5
This file contains all the information available in the dataset in HDF5 file format.The data of each individual station for the complete history of it can be accessed using the station ID. Inside, each dataframe contains an entry per hour, which includes the levels of all the measures that station can perform. Each individual dataframe contains one row per entry, marked by a timestamp. The columns include the levels of each possible measurement in such station (refer to the dataset description for more information about the measurements). This file also contains master, the dataframe that includes all the information available about the current stations. The same information can also be found in the file stations.csv.

### station_dataset_visualization.ipynb
Plots count-plots, box-and-whisker-plots and scatter-plots representing the data about the different stations.

### stations.csv
Contains all the information available about the different stations used in the dataset.
