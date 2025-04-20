from datetime import datetime
import numpy as np
import pandas as pd
from frontend.utils.dataframe import df, today_df, week_df


target = ['pm2_5_atm', 'pm10_0_atm', 'aqi']
### The pm 2.5 atm level group by weather condition and weather main

def mode_func(x):
    return x.mode().iloc[0] if not x.mode().empty else np.nan


def create_groupby(gb: str, value: str, start_datetime: datetime=None, end_datetime: datetime=None, init_df=df):
    df = init_df.copy()
    if start_datetime:
        df = df[df['ts'] >= start_datetime]
    if end_datetime:
        df = df[df['ts'] < end_datetime]

    if len(df) == 0:
        return None

    if gb:
        return df.groupby(by=gb)[value].agg(
                    mean='mean',
                    median='median',
                    mode=mode_func,
                    min='min',
                    max='max'
                ).reset_index()
    else:
        return df[value].agg(
                    mean='mean',
                    median='median',
                    mode=mode_func,
                    min='min',
                    max='max'
                ).to_frame().T.reset_index(drop=True)


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


def join_statistics(gb, **kwargs):
    gb_df = create_groupby(gb, **kwargs)

    if gb_df is None:
        return None

    gb_df = gb_df.reset_index(drop=True)

    if gb is None:
        stats = gb_df.T.reset_index()
        stats.rename(columns={'index': 'stat', 0: 'value'}, inplace=True)
        return stats

    stats = pd.melt(
        gb_df,
        id_vars=[gb],
        value_vars=['mean', 'median', 'mode', 'min', 'max'],
        var_name='stat',
        value_name='value'
    )

    return stats




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

parse_attr = {
        'Timestamp': 'ts',
        'PM 1.0': 'pm1_0_atm',
        'PM 2.5': 'pm2_5_atm',
        'PM 10': 'pm10_0_atm',
        'AQI': 'aqi',
        "Particles > 0.3 μm": "pcnt_0_3",
        "Particles > 0.5 μm": "pcnt_0_5",
        "Particles > 1.0 μm": "pcnt_1_0",
        "Particles > 2.5 μm": "pcnt_2_5",
        "Particles > 5.0 μm": "pcnt_5_0",
        "Particles > 10.0 μm": "pcnt_10_0",
        'Temperature': 'temp',
        'Humidity': 'hum',
        'Wind Speed': 'wind_spd',
        'Light': 'light',
        'Cloud': 'cloud',
        'Rainfall': 'rain',
    }

parse_hue = {
        'None': None,
        'Weather': 'weather_main',
        'Weather (Detailed)': 'weather_con',
        'Day of Week': 'day_of_week'
    }
### Find Peaked and Bottom date
def find_peaked_and_bottomed(init_col: str, init_df: pd.DataFrame = df):
    df = init_df.copy()

    col = parse_attr[init_col]

    peak_value = df[col].max()
    bottom_value = df[col].min()
    peak_rows = df[df[col] == peak_value]
    bottom_rows = df[df[col] == bottom_value]

    peak_record = peak_rows.iloc[-1].to_frame().T.reset_index(drop=True)[['ts']+show_col]
    bottom_record = bottom_rows.iloc[-1].to_frame().T.reset_index(drop=True)[['ts']+show_col]

    peak_time = peak_record['ts'][0].strftime('%d %b %Y, %I:%M %p')
    bottom_time = bottom_record['ts'][0].strftime('%d %b %Y, %I:%M %p')

    return peak_record, peak_value, peak_time, bottom_record, bottom_value, bottom_time


### Datetime
min_datetime = df['ts'].min().to_pydatetime()
max_datetime = df['ts'].max().to_pydatetime()
