import plotly.express as px
from frontend.utils.dataframe import df, today_df, week_df


aqi_ts = px.line(df, x='ts', y= 'aqi', title='AQI Line Chart')

aqi_ts_today = px.line(today_df, x='ts', y= 'aqi', title='AQI Line Chart')

aqi_ts_week = px.line(week_df, x='ts', y= 'aqi', title='AQI Line Chart')

####
pm_atm = ["pm1_0_atm", "pm2_5_atm", "pm10_0_atm"]
original_categorical = ["weather_main", "weather_con", "day_of_week"]


### Line graph of pm atm

df['date'] = df['ts'].dt.to_timestamp()

pm_ts = px.line(
    df.sort_values('date'),
    x='date',
    y=pm_atm,
    title='pm 1.0 atm vs pm 2.5 atm vs pm 10.0 atm Over Time',
    labels={'date': 'Date', 'pm1_0_atm': 'pm 1.0 atm', 'pm2_5_atm': 'pm 2.5 atm', 'pm10_0_atm': 'pm 10.0 atm'},
    width=1300,
    height=450
)

df.drop('date', axis=1, inplace=True)
