import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
get_ipython().run_line_magic("matplotlib", " inline")


# ignore warnings
import warnings
warnings.filterwarnings("ignore")
pd.set_option('mode.chained_assignment', None) 


# importing extensions for glob files
from os.path import exists
import glob

# feather file exist or not
file_exists = exists('data/aqi_data.feather')

# if feather file dose not exist then load all the csv files, merge csv files into one and save the merged file as feather file
if(not file_exists):
    files = glob.glob("data/csvs_per_year/*.csv")
    for index,file in enumerate(files):
        files[index] = pd.read_csv(file)
    raw_df = pd.concat(files)
    raw_df.to_feather('data/aqi_data.feather')
    del(raw_df)

# loading the feather file
raw_df = pd.read_feather('data/aqi_data.feather')

# parsing the date column as datetime
raw_df['date'] = pd.to_datetime(raw_df['date'])

# setting the date column as datetime
raw_df = raw_df.set_index('date')


raw_df.info(show_counts=True, memory_usage=True)


raw_df.describe()


raw_df.head()


raw_df.tail()


null_ratio_df = pd.DataFrame(round(raw_df.isnull().sum() * 100 / raw_df.shape[0],2).sort_values(ascending = False),columns=['Null Ratio'])
null_ratio_df


columns_to_keep = list(null_ratio_df[null_ratio_df['Null Ratio'] < 40].index)
columns_to_keep


aqi_df = raw_df[columns_to_keep]


aqi_df['year'] = aqi_df.index.copy().year
aqi_df['month'] = aqi_df.index.copy().month
aqi_df['day'] = aqi_df.index.copy().day
aqi_df['hour'] = aqi_df.index.copy().hour


aqi_df


from plotly.subplots import make_subplots
import plotly.graph_objs as go


yearly_df = aqi_df.groupby('year')[columns_to_keep].mean().copy()
monthly_df = aqi_df.groupby('month')[columns_to_keep].mean().copy()
daily_df = aqi_df.groupby('day')[columns_to_keep].mean().copy()
hourly_df = aqi_df.groupby('hour')[columns_to_keep].mean().copy()


for col in columns_to_keep:
    if col get_ipython().getoutput("= 'station':")
        fig = make_subplots(rows=2, cols=2)
        fig.add_trace(
            go.Scatter(x=yearly_df.index, y=yearly_df[col],mode="lines",name='yealy'),
            row=1, col=1
        )
        fig.add_trace(
            go.Scatter(x=monthly_df.index, y=monthly_df[col],mode="lines",name='monthy'),
            row=1, col=2
        )
        fig.add_trace(
            go.Scatter(x=daily_df.index, y=daily_df[col],mode="lines",name='daily'),
            row=2, col=1
        )
        fig.add_trace(
            go.Scatter(x=hourly_df.index, y=hourly_df[col],mode="lines",name='hourly'),
            row=2, col=2
        )
        fig.update_layout(title_text=f"{col}")
        fig.show()


aqi_df.iloc[:,aqi_df.columns get_ipython().getoutput("= 'station'] = aqi_df.groupby('station').transform(lambda x: x.fillna(x.mean())).copy()")


aqi_df.iloc[:,aqi_df.columns get_ipython().getoutput("= 'month'] = aqi_df.groupby('month').transform(lambda x: x.fillna(x.mean())).copy()")


yearly_df = aqi_df.groupby('year')[columns_to_keep].mean().copy()
monthly_df = aqi_df.groupby('month')[columns_to_keep].mean().copy()
daily_df = aqi_df.groupby('day')[columns_to_keep].mean().copy()
hourly_df = aqi_df.groupby('hour')[columns_to_keep].mean().copy()


for col in columns_to_keep:
    if col get_ipython().getoutput("= 'station':")
        fig = make_subplots(rows=2, cols=2)
        fig.add_trace(
            go.Scatter(x=yearly_df.index, y=yearly_df[col],mode="lines", name='yealy'),
            row=1, col=1
        )
        fig.add_trace(
            go.Scatter(x=monthly_df.index, y=monthly_df[col],mode="lines", name='monthy'),
            row=1, col=2
        )
        fig.add_trace(
            go.Scatter(x=daily_df.index, y=daily_df[col],mode="lines", name='daily'),
            row=2, col=1
        )
        fig.add_trace(
            go.Scatter(x=hourly_df.index, y=hourly_df[col],mode="lines", name='hourly'),
            row=2, col=2
        )
        fig.update_layout(title_text=f"{col}")
        fig.show()


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

aqi_df["PM10_24hr_avg"] = aqi_df.groupby("station")["PM10"].rolling(window = 24, min_periods = 1).mean().copy().values
aqi_df["PM10_SubIndex"] = aqi_df["PM10_24hr_avg"].apply(lambda x: get_PM10_subindex(x)).copy()


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

aqi_df["SO2_24hr_avg"] = aqi_df.groupby("station")["SO_2"].rolling(window = 24, min_periods = 1).mean().copy().values
aqi_df["SO2_SubIndex"] = aqi_df["SO2_24hr_avg"].apply(lambda x: get_SO2_subindex(x)).copy()


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

    
aqi_df["NOx_24hr_avg"] = aqi_df.groupby("station")["NOx"].rolling(window = 24, min_periods = 1).mean().copy().values
aqi_df["NOx_SubIndex"] = aqi_df["NOx_24hr_avg"].apply(lambda x: get_NOx_subindex(x)).copy()


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

aqi_df["CO_8hr_max"] = aqi_df.groupby("station")["CO"].rolling(window = 8, min_periods = 1).max().copy().values
aqi_df["CO_SubIndex"] = aqi_df["CO_8hr_max"].apply(lambda x: get_CO_subindex(x)).copy()


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

aqi_df["O3_8hr_max"] = aqi_df.groupby("station")["O_3"].rolling(window = 8, min_periods = 1).max().copy().values
aqi_df["O3_SubIndex"] = aqi_df["O3_8hr_max"].apply(lambda x: get_O3_subindex(x)).copy()


aqi_df["aqi"] = round(aqi_df[["PM10_SubIndex","SO2_SubIndex","NOx_SubIndex", "CO_SubIndex", "O3_SubIndex"]].max(axis = 1))


final_aqi_df = aqi_df[['NOx', 'CO', 'SO_2', 'PM10', 'O_3', 'NO_2', 'station', 'year', 'month','day', 'hour','aqi']].copy()


temp_aqi = final_aqi_df.resample('Y').mean()
px.line(
    x=temp_aqi.index,
    y=temp_aqi["aqi"]
)


temp_aqi = final_aqi_df.resample('Q').mean()
px.line(
    x=temp_aqi.index,
    y=temp_aqi["aqi"]
)


temp_aqi = final_aqi_df.resample('M').mean()
px.line(
    x=temp_aqi.index,
    y=temp_aqi["aqi"]
)


get_ipython().getoutput("pip install pmdarima --quiet")


aqi = final_aqi_df.resample('M').mean()[['aqi']]
test_len = 12
print(f'shape of data : {aqi.shape}')


from pmdarima.arima import ADFTest
adf_test = ADFTest(alpha = 0.07)
adf_test.should_diff(aqi['aqi'])


from statsmodels.tsa.seasonal import seasonal_decompose
result = seasonal_decompose(aqi['aqi'])
result.plot()


from pmdarima import auto_arima
setwise_fit = auto_arima(aqi['aqi'], start_p=0, max_p=5, d=1, max_d=5, start_q=0, max_q=5, start_P=0, max_P=5, D=1, max_D=5, start_Q=0, max_Q=5, 
                         m=12, seasonal=True,error_action='warn',trace=False, suppress_warnings=True, stepwise=True, random_state=True,n_fits=50)
setwise_fit.summary()


train = aqi.iloc[:-test_len]
test = aqi.iloc[-test_len:]
print(f"train : {train.shape}")
print(f"test : {test.shape}")


from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error

# start and end
start=len(train)
end=len(train)+len(test)-1

# model
model = ARIMA(train['aqi'],order=(5,1,1), seasonal_order=(3, 1, 0, 12))
model = model.fit()
# method_kwargs={"warn_convergence": False}

#prediction
pred = model.predict(start=start, end=end)

# plot predicted vs actual
pred.plot(legend=True)
test['aqi'].plot(legend=True)

# root mean square error of model
from math import sqrt
rsme = sqrt(mean_squared_error(pred,test['aqi']))
print(f"mean of test df : {test['aqi'].mean()}")
print(f'resme : {rsme}')


model = ARIMA(aqi['aqi'],order=(5,1,1), seasonal_order=(3, 1, 0, 12))
model = model.fit()


# 36 months future
start = len(aqi)
end = len(aqi) + 36
pred = model.predict(start=start, end=end)
px.line(x=aqi['aqi'])
pred.plot(legend=True)
aqi['aqi'].plot(legend=True)
