import plotly.express as px
from frontend.utils.dataframe import df, today_df, week_df


aqi_ts = px.line(df, x='ts', y= 'aqi', labels={'ts': 'Timestamp', 'aqi': "AQI"}, title='AQI Line Chart')

aqi_ts_today = px.line(today_df, x='ts', y= 'aqi', labels={'ts': 'Timestamp', 'aqi': "AQI"}, title='AQI Line Chart')

aqi_ts_week = px.line(week_df, x='ts', y= 'aqi', labels={'ts': 'Timestamp', 'aqi': "AQI"}, title='AQI Line Chart')


####
pm_atm = ["pm1_0_atm", "pm2_5_atm", "pm10_0_atm"]
original_categorical = ["weather_main", "weather_con", "day_of_week"]


### Line graph of pm atm

pm_ts = px.line(
    df,
    x='ts',
    y=pm_atm,
    title='Particulate Matter Over Time',
    labels={'ts': 'Timestamp', 'pm1_0_atm': 'PM 1.0', 'pm2_5_atm': 'PM 2.5', 'pm10_0_atm': 'PM 10', 'value': 'Particulate Matter concentration (µg/m³)'},
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
