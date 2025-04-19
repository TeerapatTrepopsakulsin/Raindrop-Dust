import numpy as np
import pandas as pd

from frontend.utils.dataframe import df, today_df, week_df


target = ['pm2_5_atm', 'pm10_0_atm', 'aqi']
### The pm 2.5 atm level group by weather condition and weather main

def mode_func(x):
    return x.mode().iloc[0] if not x.mode().empty else np.nan


def create_groupby(gb: str, value: str):
    return df.groupby(gb)[value].agg(
                mean='mean',
                median='median',
                mode=mode_func,
                min='min',
                max='max'
            ).reset_index()


def join_pm_aqi(pm2_5, pm10_0, aqi, gb):
    pm2_5 = pm2_5.copy()
    pm10_0 = pm10_0.copy()
    aqi = aqi.copy()

    pm2_5['type'] = 'pm2_5_atm'
    pm10_0['type'] = 'pm10_0_atm'
    aqi['type'] = 'aqi'

    pm = pd.concat([pm2_5, pm10_0], axis=0, ignore_index=True)
    pm_aqi = pd.concat([pm, aqi], axis=0, ignore_index=True)

    order = [gb, 'type', 'mean', 'median', 'mode', 'min', 'max']

    return pm_aqi[order]


# by weather condition
pm2_5_weather_con = create_groupby('weather_con', 'pm2_5_atm')
pm10_0_weather_con = create_groupby('weather_con', 'pm10_0_atm')
aqi_weather_con = create_groupby('weather_con', 'aqi')
pm_aqi_weather_con = join_pm_aqi(pm2_5_weather_con, pm10_0_weather_con, aqi_weather_con, 'weather_con')


# by weather main
pm2_5_weather_main = create_groupby('weather_main', 'pm2_5_atm')
pm10_0_weather_main = create_groupby('weather_main', 'pm10_0_atm')
aqi_weather_main = create_groupby('weather_main', 'aqi')
pm_aqi_weather_main = join_pm_aqi(pm2_5_weather_main, pm10_0_weather_main, aqi_weather_main, 'weather_main')


# by day of week
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

pm2_5_day_of_week = create_groupby("day_of_week", 'pm2_5_atm')
pm10_0_day_of_week = create_groupby("day_of_week", 'pm10_0_atm')
aqi_day_of_week = create_groupby("day_of_week", 'aqi')
pm_aqi_day_of_week = join_pm_aqi(pm2_5_day_of_week, pm10_0_day_of_week, aqi_day_of_week, 'day_of_week')

pm2_5_day_of_week['day_of_week'] = pd.Categorical(
    pm2_5_day_of_week['day_of_week'],
    categories=days_order,
    ordered=True
)
pm2_5_day_of_week = pm2_5_day_of_week.sort_values('day_of_week')
pm2_5_day_of_week.reset_index(drop=True, inplace=True)

# PM 2.5 vs Rain
pm2_5_rain = df.groupby('is_rain')['pm2_5_atm'].agg(['mean', 'median', 'min', 'max', 'std']).reset_index()
pm2_5_rain['is_rain'] = pm2_5_rain['is_rain'].map({True: 'Rain', False: 'No Rain'})


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

envi_col = [
    "temp",
    "hum",
    "light",
    "aqi",
    "pm2_5_atm",
    "pm10_0_atm",
    "cloud",
    "rain",
    "wind_spd"
]

### Correlation of environmental attribute
envi_corr = df[envi_col].corr()

### Today
# Summary
today = today_df[show_col].describe()

# Latest
latest = df.iloc[-1]
prev = df.iloc[-2]
delta = latest[show_col] - prev[show_col]

### This Week
week = week_df[show_col].describe()

