import plotly.express as px
from frontend.utils.dataframe import df, today_df


aqi_ts = px.line(df, x='ts', y= 'aqi', title='AQI Line Chart')

aqi_ts_today = px.line(today_df, x='ts', y= 'aqi', title='AQI Line Chart')
