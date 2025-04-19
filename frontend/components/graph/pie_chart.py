import plotly.express as px
from .stats import pm2_5_weather_main, pm2_5_weather_con, pm2_5_day_of_week


def pie_title(name: str, value: str) -> str:
    return f'Average {value} for each {name}'


pm2_5_weather_main = px.pie(
    pm2_5_weather_main,
    names='weather_main',
    values='mean',
    title=pie_title("Weather Condition", "PM 2.5"),
    color_discrete_sequence=px.colors.sequential.Rainbow,
)


pm2_5_weather_con = px.pie(
    pm2_5_weather_con,
    names='weather_con',
    values='mean',
    title=pie_title("Weather Condition", "PM 2.5"),
    color_discrete_sequence=px.colors.sequential.Rainbow,
)


pm2_5_day_of_week = px.pie(
    pm2_5_day_of_week,
    names='day_of_week',
    values='mean',
    title=pie_title("Day of Week", "PM 2.5"),
    color_discrete_sequence=px.colors.sequential.Rainbow,
)
