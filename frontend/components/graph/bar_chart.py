import plotly.express as px
from frontend.utils.dataframe import df
from .stats import pm_aqi_weather_main, target, pm_aqi_weather_con, pm_aqi_day_of_week

### PM2.5 when rain and not rain

pm25_rain_stats = df.groupby('is_rain')['pm2_5_atm'].agg(['mean', 'median', 'min', 'max', 'std']).reset_index()
pm25_rain_stats['is_rain'] = pm25_rain_stats['is_rain'].map({True: 'Rain', False: 'No Rain'})
df['is_rain_label'] = df['is_rain'].map({True: 'Rain', False: 'No Rain'})

pm2_5_rain = px.bar(pm25_rain_stats,
             x='is_rain',
             y='mean',
             title='PM 2.5: Rain vs No Rain',
             labels={'is_rain': 'Rain Condition', 'mean': 'Average PM 2.5 (μg/m^3)'})
pm2_5_rain.update_layout(width=800, height=600)

df.drop('is_rain_label', axis=1, inplace=True)


### Weather main

pm_aqi_weather_main = px.bar(
    pm_aqi_weather_main,
    x='type',
    y='mean',
    title='Average Air Quality for each Weather Condition',
    labels={'type': '',
            'mean': 'Average PM concentration (μg/m^3) / Average AQI',
            'weather_main': 'Weather Condition',
            'pm2_5_atm': 'PM 2.5'},
    color='weather_main',
    barmode='group',
)

### Weather con

pm_aqi_weather_con = px.bar(
    pm_aqi_weather_con,
    x='type',
    y='mean',
    title='Average Air Quality for each Weather Condition',
    labels={'type': '',
            'mean': 'Average PM concentration (μg/m^3) / Average AQI',
            'weather_con': 'Weather Condition',
            'pm2_5_atm': 'PM 2.5'},
    color='weather_con',
    barmode='group',
)

### Day of Week

pm_aqi_day_of_week = px.bar(
    pm_aqi_day_of_week,
    x='type',
    y='mean',
    title='Average Air Quality for each Day of Week',
    labels={'type': '',
            'mean': 'Average PM concentration (μg/m^3) / Average AQI',
            'day_of_week': 'Weather Condition',
            'pm2_5_atm': 'PM 2.5'},
    color='day_of_week',
    barmode='group',
)
