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



Topic: Air Quality in Madrid (2001–2018) Dataset
In Madrid, the high levels of pollution during certain dry periods has forced the authorities to take measures to improve the air quality in the city center.
Thanks to the publicly available historical data of the levels registered from 2001-2018. 
All the data we used for this project was pre cleaned and made available. But we learnt that not every station in the dataset has the same equipment therefore each station can only measure a certain subset of air polluting particles.
The complete list of possible measurements and their explanations are:


* SO_2: sulphur dioxide level measured in μg/m³. High levels of sulphur dioxide can produce irritation in the skin and membranes, and worsen asthma or heart diseases in sensitive groups.
* CO: carbon monoxide level measured in mg/m³. Carbon monoxide poisoning involves headaches, dizziness and confusion in short exposures and can result in loss of consciousness, arrhythmias, seizures or even death in the long term.
* NO: nitric oxide level measured in μg/m³. This is a highly corrosive gas generated among others by motor vehicles and fuel burning processes.
* NO_2: nitrogen dioxide level measured in μg/m³. Long-term exposure is a cause of chronic lung diseases, and are harmful for the vegetation.
* PM25: particles smaller than 2.5 μm level measured in μg/m³. The size of these particles allow them to penetrate into the gas exchange regions of the lungs (alveolus) and even enter the arteries. Long-term exposure is proven to be related to low birth weight and high blood pressure in newborn babies.
* PM10: particles smaller than 10 μm. Even though they cannot penetrate the alveolus, they can still penetrate through the lungs and affect other organs. Long term exposure can result in lung cancer and cardiovascular complications.
* NOx: nitrous oxides level measured in μg/m³. Affect the human respiratory system worsening asthma or other diseases, and are responsible for the yellowish-brown color of photochemical smog.
* O_3: ozone level measured in μg/m³. High levels can produce asthma, bronchitis or other chronic pulmonary diseases in sensitive groups or outdoor workers.
* TOL: toluene (methylbenzene) level measured in μg/m³. Long-term exposure to this substance (present in tobacco smoke as well) can result in kidney complications or permanent brain damage.
* BEN: benzene level measured in μg/m³. Benzene is an eye and skin irritant, and long exposures may result in several types of cancer, leukemia and anemia. Benzene is considered a group 1 carcinogenic to humans by the IARC.
* EBE: ethylbenzene level measured in μg/m³. Long term exposure can cause hearing or kidney problems and the IARC has concluded that long-term exposure can produce cancer.
* MXY: m-xylene level measured in μg/m³. Xylenes can affect not only air but also water and soil, and a long exposure to high levels of xylenes can result in diseases affecting the liver, kidney and nervous system (especially memory and affected stimulus reaction).
* PXY: p-xylene level measured in μg/m³. See MXY for xylene exposure effects on health.
* OXY: o-xylene level measured in μg/m³. See MXY for xylene exposure effects on health.
* TCH: total hydrocarbons level measured in mg/m³. This group of substances can be responsible for different blood, immune system, liver, spleen, kidneys or lung diseases.
* CH4: methane level measured in mg/m³. This gas is an asphyxiant, which displaces the oxygen animals need to breathe. Displaced oxygen can result in dizziness, weakness, nausea and loss of coordination.
* NMHC: non-methane hydrocarbons (volatile organic compounds) level measured in mg/m³. Long exposure to some of these substances can result in damage to the liver, kidney, and central nervous system. Some of them are suspected to cause cancer in humans.
From our analysis, we’ve been able to answer
-> How do different gases correlate their levels?
-> Are they any changes in the trends?
-> can they be mapped to the recent decisions made by the city council or do they relate to rainy dates?
-> what is the best model to predict pollution levels?
-> how do the levels interpolate between the location of the station?
-> are some gases more common at different locations?