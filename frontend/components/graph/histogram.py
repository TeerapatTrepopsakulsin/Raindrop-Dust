import plotly.express as px
from frontend.utils.dataframe import df

### Histogram for pm atm

# pm histogram with no hue
pm1_0 = px.histogram(df, x="pm1_0_atm", title=f"Histogram of PM 1.0", histnorm='percent', width=1000, height=400)
pm2_5 = px.histogram(df, x="pm1_0_atm", title=f"Histogram of PM 2.5", histnorm='percent', width=1000, height=400)
pm10_0 = px.histogram(df, x="pm10_0_atm", title=f"Histogram of PM 10", histnorm='percent', width=1000, height=400)
aqi = px.histogram(df, x="aqi", title=f"Histogram of AQI", histnorm='percent', width=1000, height=400)


### Histogram for pm atm with categorical data

# pm1_0_atm histograms
pm1_0_weather_main = px.histogram(
    df, x="pm1_0_atm", title="Histogram of pm1_0_atm", color="weather_main", width=1000, height=300
)

pm1_0_weather_con = px.histogram(
    df, x="pm1_0_atm", title="Histogram of pm1_0_atm", color="weather_con", width=1000, height=300
)

pm1_0_day_of_week = px.histogram(
    df, x="pm1_0_atm", title="Histogram of pm1_0_atm", color="day_of_week", width=1000, height=300
)


# pm2_5_atm histograms
pm2_5_weather_main = px.histogram(
    df, x="pm2_5_atm", title="Histogram of pm2_5_atm", color="weather_main", width=1000, height=300
)

pm2_5_weather_con = px.histogram(
    df, x="pm2_5_atm", title="Histogram of pm2_5_atm", color="weather_con", width=1000, height=300
)

pm2_5_day_of_week = px.histogram(
    df, x="pm2_5_atm", title="Histogram of pm2_5_atm", color="day_of_week", width=1000, height=300
)


# pm10_0_atm histograms
pm10_0_weather_main = px.histogram(
    df, x="pm10_0_atm", title="Histogram of pm10_0_atm", color="weather_main", width=1000, height=300
)

pm10_0_weather_con = px.histogram(
    df, x="pm10_0_atm", title="Histogram of pm10_0_atm", color="weather_con", width=1000, height=300
)

pm10_0_day_of_week = px.histogram(
    df, x="pm10_0_atm", title="Histogram of pm10_0_atm", color="day_of_week", width=1000, height=300
)


# Frequency histograms for categorical attributes

weather_main = px.histogram(df, x="weather_main", title="Frequency of weather_main", width=1000, height=300)
weather_con = px.histogram(df, x="weather_con", title="Frequency of weather_con", width=1000, height=300)
day_of_week = px.histogram(df, x="day_of_week", title="Frequency of day_of_week", width=1000, height=300)
