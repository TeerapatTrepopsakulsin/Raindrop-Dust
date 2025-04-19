import plotly.express as px
from frontend.utils.dataframe import df, today_df, week_df


### Scatter chart:

## No hue
# humidity vs pm 2.5 atm
pm2_5_hum = px.scatter(
    df,
    x='hum',
    y='pm2_5_atm',
    trendline='ols',
    width=1000,
    height=400,
    title='Humidity vs PM 2.5',
    labels={'hum': 'Humidity', 'pm2_5_atm': 'PM 2.5'}
)

# rain vs pm 2.5 atm
pm2_5_rain = px.scatter(
    df,
    x='rain',
    y='pm2_5_atm',
    trendline='ols',
    width=1000,
    height=400,
    title='Rain vs PM 2.5',
    labels={'rain': 'Rain', 'pm2_5_atm': 'PM 2.5'}
)

# temperature vs pm 2.5 atm
pm2_5_temp = px.scatter(
    df,
    x='temp',
    y='pm2_5_atm',
    trendline='ols',
    width=1000,
    height=400,
    title='Temperature vs PM 2.5',
    labels={'temp': 'Temperature', 'pm2_5_atm': 'PM 2.5'}
)

# wind speed vs pm 2.5 atm
pm2_5_wind = px.scatter(
    df,
    x='wind_spd',
    y='pm2_5_atm',
    trendline='ols',
    width=1000,
    height=400,
    title='Wind Speed vs PM 2.5',
    labels={'wind_spd': 'Wind Speed', 'pm2_5_atm': 'PM 2.5'}
)

# light vs pm 2.5 atm
pm2_5_light = px.scatter(
    df,
    x='light',
    y='pm2_5_atm',
    trendline='ols',
    width=1000,
    height=400,
    title='Light vs PM 2.5',
    labels={'light': 'Light', 'pm2_5_atm': 'PM 2.5'}
)

# cloud vs PM 2.5
pm2_5_cloud = px.scatter(
    df,
    x='cloud',
    y='pm2_5_atm',
    trendline='ols',
    width=1000,
    height=400,
    title='Cloud vs PM 2.5',
    labels={'cloud': 'Cloud', 'pm2_5_atm': 'PM 2.5'}
)


## Weather Condition as hue
# humidity vs pm 2.5 atm
pm2_5_hum_weather = px.scatter(
    df,
    x='hum',
    y='pm2_5_atm',
    color='weather_con',
    trendline='ols',
    width=1000,
    height=400,
    title='Humidity vs PM 2.5',
    labels={'hum': 'Humidity', 'pm2_5_atm': 'PM 2.5'}
)
pm2_5_hum_weather.update_layout(legend_title_text='Weather Condition')

# rain vs pm 2.5 atm
pm2_5_rain_weather = px.scatter(
    df,
    x='rain',
    y='pm2_5_atm',
    color='weather_con',
    trendline='ols',
    width=1000,
    height=400,
    title='Rain vs PM 2.5',
    labels={'rain': 'Rain', 'pm2_5_atm': 'PM 2.5'}
)
pm2_5_rain_weather.update_layout(legend_title_text='Weather Condition')

# temperature vs pm 2.5 atm
pm2_5_temp_weather = px.scatter(
    df,
    x='temp',
    y='pm2_5_atm',
    color='weather_con',
    trendline='ols',
    width=1000,
    height=400,
    title='Temperature vs PM 2.5',
    labels={'temp': 'Temperature', 'pm2_5_atm': 'PM 2.5'}
)
pm2_5_temp_weather.update_layout(legend_title_text='Weather Condition')

# wind speed vs pm 2.5 atm
pm2_5_wind_weather = px.scatter(
    df,
    x='wind_spd',
    y='pm2_5_atm',
    color='weather_con',
    trendline='ols',
    width=1000,
    height=400,
    title='Wind Speed vs PM 2.5',
    labels={'wind_spd': 'Wind Speed', 'pm2_5_atm': 'PM 2.5'}
)
pm2_5_wind_weather.update_layout(legend_title_text='Weather Condition')

# light vs pm 2.5 atm
pm2_5_light_weather = px.scatter(
    df,
    x='light',
    y='pm2_5_atm',
    color='weather_con',
    trendline='ols',
    width=1000,
    height=400,
    title='Light vs PM 2.5',
    labels={'light': 'Light', 'pm2_5_atm': 'PM 2.5'}
)
pm2_5_light_weather.update_layout(legend_title_text='Weather Condition')

# cloud vs PM 2.5
pm2_5_cloud_weather = px.scatter(
    df,
    x='cloud',
    y='pm2_5_atm',
    color='weather_con',
    trendline='ols',
    width=1000,
    height=400,
    title='Cloud vs PM 2.5',
    labels={'cloud': 'Cloud', 'pm2_5_atm': 'PM 2.5'}
)
pm2_5_cloud_weather.update_layout(legend_title_text='Weather Condition')

### Scatter plot for pm atm
pm_atm = ["pm1_0_atm", "pm2_5_atm", "pm10_0_atm"]

pm_matrix = px.scatter_matrix(df, dimensions=pm_atm, width=800, height=800)
