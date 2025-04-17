import numpy as np
from frontend.utils.dataframe import df, today_df, week_df


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

show_col = [
    "temp",
    "min_temp",
    "max_temp",
    "hum",
    "light",
    "aqi",
    "pm1_0_atm",
    "pm2_5_atm",
    "pm10_0_atm",
    "pm1_0",
    "pm2_5",
    "pm10_0",
    "pcnt_0_3",
    "pcnt_0_5",
    "pcnt_1_0",
    "pcnt_2_5",
    "pcnt_5_0",
    "pcnt_10_0",
    "cloud",
    "rain",
    "wind_spd"
]

### Correlation of numerical attributes
corr = df[show_col].corr()

### Today
# Summary
today = today_df[show_col].describe()

# Latest
latest = df.iloc[-1]
prev = df.iloc[-2]
delta = latest[show_col] - prev[show_col]

### This Week
week = week_df[show_col].describe()

