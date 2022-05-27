# Air Quality in Madrid (Different pollution levels in Madrid from 2001-2018)

This dataset is created out of the frustation of how inconvenient and irregular the historical data was provided in the Open Data website. It contains in a practical format 18 years (2001-2018) of hourly data in just a single file, which makes this dataset a great playground for time series analysis and other prediction tasks. How do different gases correlate their levels? Are there any changes in trends? Can they be mapped to the recent decisions made by the city council, or do they relate to rainy dates? What is the best model to predict pollution levels? How do the levels interpolate between the location of the stations? Are some gases more common at different elevations?

## Different files in the project are as follows:

### Project_Documentation.txt
Explains the different measurements present in the provided dataset. It also stated the different answers that we are able to obtain from our analysis.

### W706.ipynb
Contains the main file of the project. Its contents are : (1) Handling NaN Values (2) Removing unnecessary features (3) Exploring the Cleaned DataFrame (4) AQI Calculation (5) Visualization of Variables

### dataset_visualization.ipynb
Plots heatmaps based on the datasets provided with respect to different years.

### stations.csv
Contains all the information available about the different stations used in the dataset.

### csv_per_year
Contains each year wather dataset.