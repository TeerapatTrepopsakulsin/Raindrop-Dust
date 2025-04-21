import plotly.express as px
from frontend.utils.dataframe import df, today_df, week_df, forecast_1d_df, forecast_3d_df


### AQI
aqi_ts = px.line(df, x='ts', y='aqi', labels={'ts': 'Timestamp', 'aqi': "AQI"}, title='AQI Line Chart')

aqi_ts_today = px.line(today_df, x='ts', y='aqi', labels={'ts': 'Timestamp', 'aqi': "AQI"}, title='AQI Line Chart Today')

aqi_ts_week = px.line(week_df, x='ts', y='aqi', labels={'ts': 'Timestamp', 'aqi': "AQI"}, title='AQI Line Chart This Week')


####
original_categorical = ["weather_main", "weather_con", "day_of_week"]

df = df.rename(columns={"pm1_0_atm": "PM 1.0", "pm2_5_atm": "PM 2.5", "pm10_0_atm": "PM 10"})
today_df = today_df.rename(columns={"pm1_0_atm": "PM 1.0", "pm2_5_atm": "PM 2.5", "pm10_0_atm": "PM 10"})
week_df = week_df.rename(columns={"pm1_0_atm": "PM 1.0", "pm2_5_atm": "PM 2.5", "pm10_0_atm": "PM 10"})
pm_atm = ["PM 1.0", "PM 2.5", "PM 10"]


### Line graph of pm atm

pm_ts = px.line(
    df,
    x='ts',
    y=pm_atm,
    title='Particulate Matter Over Time',
    labels={
        'ts': 'Timestamp',
        'pm1_0_atm': 'PM 1.0',
        'pm2_5_atm': 'PM 2.5',
        'pm10_0_atm': 'PM 10',
        'value': 'Particulate Matter concentration (µg/m³)',
        'variable': 'PM Type'
    },
    width=1300,
    height=450
)

pm_ts_today = px.line(
    today_df,
    x='ts',
    y=pm_atm,
    title='Particulate Matter Today',
    labels={
        'ts': 'Timestamp',
        'pm1_0_atm': 'PM 1.0',
        'pm2_5_atm': 'PM 2.5',
        'pm10_0_atm': 'PM 10',
        'value': 'Particulate Matter concentration (µg/m³)',
        'variable': 'PM Type'
    },
    width=1300,
    height=450
)


pm_ts_week = px.line(
    week_df,
    x='ts',
    y=pm_atm,
    title='Particulate Matter This Week',
    labels={'ts': 'Timestamp', 'pm1_0_atm': 'PM 1.0', 'pm2_5_atm': 'PM 2.5', 'pm10_0_atm': 'PM 10', 'value': 'Particulate Matter concentration (µg/m³)'},
    width=1300,
    height=450
)


### Forecasting
forecast_1d_df = forecast_1d_df.rename(columns={"aqi": "AQI", "pm2_5": "PM 2.5", "pm10_0": "PM 10"})
forecast_3d_df = forecast_3d_df.rename(columns={"aqi": "AQI", "pm2_5": "PM 2.5", "pm10_0": "PM 10"})

# 1-day
pm_forecast1d = px.line(
    forecast_1d_df,
    x='timestamp',
    y=["PM 2.5", "PM 10"],
    title='Particulate Matter Forecast for the next day',
    labels={'timestamp': 'Timestamp',
            'value': 'Particulate Matter concentration (µg/m³)',
            'variable': 'PM Type'},
    width=1300,
    height=450
)

aqi_forecast1d = px.line(
    forecast_1d_df,
    x='timestamp',
    y='AQI',
    title='AQI Forecast for the next day',
    labels={'timestamp': 'Timestamp'},
    width=1300,
    height=450
)

# 3-day
pm_forecast3d = px.line(
    forecast_3d_df,
    x='timestamp',
    y=["PM 2.5", "PM 10"],
    title='Particulate Matter Forecast for the next 3 days',
    labels={'timestamp': 'Timestamp',
            'value': 'Particulate Matter concentration (µg/m³)',
            'variable': 'PM Type'},
    width=1300,
    height=450
)

aqi_forecast3d = px.line(
    forecast_3d_df,
    x='timestamp',
    y='AQI',
    title='AQI Forecast for the next 3 days',
    labels={'timestamp': 'Timestamp'},
    width=1300,
    height=450
)
