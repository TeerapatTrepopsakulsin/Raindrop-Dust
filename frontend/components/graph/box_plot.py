import plotly.express as px
import plotly.graph_objects as go
from frontend.utils.dataframe import df
from .stats import pm2_5_rain


# Box plots for pm_atm without categorical coloring

pm1_0 = px.box(df, x="pm1_0_atm", width=1000, height=300)
pm2_5 = px.box(df, x="pm2_5_atm", width=1000, height=300)
pm10_0 = px.box(df, x="pm10_0_atm", width=1000, height=300)


# Box plots for pm_atm colored by weather_main

pm1_0_weather_main = px.box(df, x="pm1_0_atm", color="weather_main", width=1000, height=300)
pm2_5_weather_main = px.box(
    df,
    x="pm2_5_atm",
    color="weather_main",
    title="PM 2.5 for each Weather Condition",
    width=1000,
    height=400
)
pm10_0_weather_main = px.box(df, x="pm10_0_atm", color="weather_main", width=1000, height=300)


# Box plots for pm_atm colored by weather_con

pm1_0_weather_con = px.box(df, x="pm1_0_atm", color="weather_con", width=1000, height=300)
pm2_5_weather_con = px.box(
    df,
    x="pm2_5_atm",
    color="weather_con",
    title="PM 2.5 for each Weather Condition",
    width=1000,
    height=400
)
pm10_0_weather_con = px.box(df, x="pm10_0_atm", color="weather_con", width=1000, height=300)


# Box plots for pm_atm colored by day_of_week

pm1_0_day_of_week = px.box(df, x="pm1_0_atm", color="day_of_week", width=1000, height=300)
pm2_5_day_of_week = px.box(
    df,
    x="pm2_5_atm",
    color="day_of_week",
    title="PM 2.5 for each Day of Week",
    width=1000,
    height=400
)
pm10_0_day_of_week = px.box(df, x="pm10_0_atm", color="day_of_week", width=1000, height=300)


### PM2.5 when rain and not rain

pm25_rain_stats = pm2_5_rain.copy()

df['is_rain_label'] = df['is_rain'].map({True: 'Rain', False: 'No Rain'})

pm2_5_rain = px.box(df,
             x='is_rain_label',
             y='pm2_5_atm',
             title='PM 2.5: Rain vs No Rain',
             labels={'is_rain_label': 'Rain Condition', 'pm2_5_atm': 'PM 2.5'})
pm2_5_rain.update_layout(width=800, height=600)
pm2_5_rain.add_trace(
go.Scatter(
        x=["No Rain", "Rain"],
        y=pm25_rain_stats['mean'].values,
        mode='markers',
        marker=dict(color='red', symbol='line-ew-open', size=100),
        name='Mean'
    )
)

df.drop('is_rain_label', axis=1, inplace=True)

### Earthquake
df['earthquake'] = (df['ts'] >= '2025-03-28 13:00') & (df['ts'] < '2025-03-29 13:00')

pm2_5_earthquake = px.box(
    df,
    x='earthquake',
    y='pm2_5_atm',
    title='Earthquake effect on PM 2.5',
    labels={
        'earthquake': '',
        'pm2_5_atm': 'PM 2.5 concentration (μg/m^3)',
        'false': 'Normal',
        'true': 'Earthquake (1 pm, 28 Mar 2025 - 1 pm, 29 Mar 2025)',
    },
)

df.drop('earthquake', axis=1, inplace=True)


### Songkran
df['songkran'] = (df['ts'] >= '2025-04-13') & (df['ts'] < '2025-04-18')

pm2_5_songkran = px.box(
    df,
    x='songkran',
    y='pm2_5_atm',
    title='Songkran Festival effect on PM 2.5',
    labels={
        'songkran': '',
        'pm2_5_atm': 'PM 2.5 concentration (μg/m^3)',
        'false': 'Normal',
        'true': 'Songkran Festival (13-17 Apr 2025)',
    },
)

df.drop('songkran', axis=1, inplace=True)
