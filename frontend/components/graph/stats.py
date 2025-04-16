import numpy as np
from frontend.utils.dataframe import df


### The pm 2.5 atm level group by weather condition and weather main

def mode_func(x):
    return x.mode().iloc[0] if not x.mode().empty else np.nan

# by weather condition
pm2_5_weather_con = df.groupby('weather_con')['pm2_5_atm'].agg(
    mean='mean',
    median='median',
    mode=mode_func,
    min='min',
    max='max'
).reset_index()

# by weather main
pm2_5_weather_main = df.groupby('weather_main')['pm2_5_atm'].agg(
    mean='mean',
    median='median',
    mode=mode_func,
    min='min',
    max='max'
).reset_index()

numerical = [
    "light",
    "aqi",
    "pm1_0",
    "pm2_5",
    "pm10_0",
    "pm1_0_atm",
    "pm2_5_atm",
    "pm10_0_atm",
    "pcnt_0_3",
    "pcnt_0_5",
    "pcnt_1_0",
    "pcnt_2_5",
    "pcnt_5_0",
    "pcnt_10_0",
    "min_temp",
    "max_temp",
    "lat",
    "lon",
    "wind_spd",
    "cloud",
    "rain"
]

### Correlation of numerical attributes
corr = df[numerical].corr()
