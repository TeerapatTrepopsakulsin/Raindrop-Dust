import plotly.express as px
from frontend.utils.dataframe import df


# Box plots for pm_atm without categorical coloring

pm1_0 = px.box(df, x="pm1_0_atm", width=1000, height=300)
pm2_5 = px.box(df, x="pm2_5_atm", width=1000, height=300)
pm10_0 = px.box(df, x="pm10_0_atm", width=1000, height=300)


# Box plots for pm_atm colored by weather_main

pm1_0_weather_main = px.box(df, x="pm1_0_atm", color="weather_main", width=1000, height=300)
pm2_5_weather_main = px.box(df, x="pm2_5_atm", color="weather_main", width=1000, height=300)
pm10_0_weather_main = px.box(df, x="pm10_0_atm", color="weather_main", width=1000, height=300)


# Box plots for pm_atm colored by weather_con

pm1_0_weather_con = px.box(df, x="pm1_0_atm", color="weather_con", width=1000, height=300)
pm2_5_weather_con = px.box(df, x="pm2_5_atm", color="weather_con", width=1000, height=300)
pm10_0_weather_con = px.box(df, x="pm10_0_atm", color="weather_con", width=1000, height=300)


# Box plots for pm_atm colored by day_of_week

pm1_0_day_of_week = px.box(df, x="pm1_0_atm", color="day_of_week", width=1000, height=300)
pm2_5_day_of_week = px.box(df, x="pm2_5_atm", color="day_of_week", width=1000, height=300)
pm10_0_day_of_week = px.box(df, x="pm10_0_atm", color="day_of_week", width=1000, height=300)


### PM2.5 when rain and not rain

pm25_rain_stats = df.groupby('is_rain')['pm2_5_atm'].agg(['mean', 'median', 'min', 'max', 'std']).reset_index()
pm25_rain_stats['is_rain'] = pm25_rain_stats['is_rain'].map({True: 'Rain', False: 'No Rain'})

df['is_rain_label'] = df['is_rain'].map({True: 'Rain', False: 'No Rain'})

pm2_5_rain = px.box(df,
             x='is_rain_label',
             y='pm2_5_atm',
             title='pm 2.5 atm levels: Rain vs No Rain',
             labels={'is_rain_label': 'Rain Condition', 'pm2_5_atm': 'pm 2.5 atm'})
pm2_5_rain.update_layout(width=800, height=600)

df.drop('is_rain_label', axis=1, inplace=True)
