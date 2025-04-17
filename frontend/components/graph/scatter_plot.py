import plotly.express as px
from frontend.utils.dataframe import df, today_df, week_df


### Scatter chart:

# humidity vs pm 2.5 atm
pm2_5_hum = px.scatter(df, x='hum', y='pm2_5_atm', title='Humidity vs pm 2.5 atm', trendline='ols', width=1000, height=300)

# rain vs pm 2.5 atm
pm2_5_rain = px.scatter(df, x='rain', y='pm2_5_atm', title='Rain vs pm 2.5 atm', trendline='ols', width=1000, height=300)

# temperature vs pm 2.5 atm
pm2_5_temp = px.scatter(df, x='temp', y='pm2_5_atm', title='Temperature vs pm 2.5 atm', trendline='ols', width=1000, height=300)

# wind speed vs pm 2.5 atm
pm2_5_wind = px.scatter(df, x='wind_spd', y='pm2_5_atm', title='Wind Speed vs pm 2.5 atm', trendline='ols', width=1000, height=300)

# light vs pm 2.5 atm
pm2_5_light = px.scatter(df, x='light', y='pm2_5_atm', title='Light vs pm 2.5 atm', trendline='ols', width=1000, height=300)


### Scatter plot for pm atm
pm_atm = ["pm1_0_atm", "pm2_5_atm", "pm10_0_atm"]

pm_matrix = px.scatter_matrix(df, dimensions=pm_atm, width=800, height=800)
