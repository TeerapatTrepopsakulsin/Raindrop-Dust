import time
import streamlit as st
from frontend.components import graph


st.header("Descriptive Data & Statistics")

# Visualise
# with st.container(border=True):
with st.expander("Air Quality Trend"):
    st.plotly_chart(graph.line_graph.pm_ts)
    st.plotly_chart(graph.line_graph.aqi_ts)

with st.expander("Distributions"):
    st.plotly_chart(graph.histogram.pm2_5)
    st.plotly_chart(graph.histogram.pm10_0)
    st.plotly_chart(graph.histogram.aqi)

with st.expander("Raindrops"):
    st.plotly_chart(graph.box_plot.pm2_5_rain)
    st.dataframe(graph.stats.pm2_5_rain)

with st.expander("Weather Condition (Main)"):
    st.plotly_chart(graph.box_plot.pm2_5_weather_main)
    st.plotly_chart(graph.bar_chart.pm_aqi_weather_main)

    col1, col2 = st.columns(2)
    col1.plotly_chart(graph.pie_chart.pm2_5_weather_main)
    col2.dataframe(graph.stats.pm_aqi_weather_main)

with st.expander("Weather Condition (Detailed)"):
    st.plotly_chart(graph.box_plot.pm2_5_weather_con)
    st.plotly_chart(graph.bar_chart.pm_aqi_weather_con)

    col1, col2 = st.columns(2)
    col1.plotly_chart(graph.pie_chart.pm2_5_weather_con)
    col2.dataframe(graph.stats.pm_aqi_weather_con)

with st.expander("Day of Week"):
    st.plotly_chart(graph.box_plot.pm2_5_day_of_week)
    st.plotly_chart(graph.bar_chart.pm_aqi_day_of_week)

    col1, col2 = st.columns(2)
    col1.plotly_chart(graph.pie_chart.pm2_5_day_of_week)
    col2.dataframe(graph.stats.pm_aqi_day_of_week)

with st.expander("Correlation"):
    use_weather_hue = st.toggle("Weather Condition as hue", value=False)

    if use_weather_hue:
        with st.spinner("Loading data..."):
            time.sleep(1)
        st.plotly_chart(graph.scatter_plot.pm2_5_hum_weather)
        st.plotly_chart(graph.scatter_plot.pm2_5_rain_weather)
        st.plotly_chart(graph.scatter_plot.pm2_5_cloud_weather)
        st.plotly_chart(graph.scatter_plot.pm2_5_wind_weather)
        st.plotly_chart(graph.scatter_plot.pm2_5_temp_weather)
        st.plotly_chart(graph.scatter_plot.pm2_5_light_weather)
    else:
        with st.spinner("Loading data..."):
            time.sleep(1)
        st.plotly_chart(graph.scatter_plot.pm2_5_hum)
        st.plotly_chart(graph.scatter_plot.pm2_5_rain)
        st.plotly_chart(graph.scatter_plot.pm2_5_cloud)
        st.plotly_chart(graph.scatter_plot.pm2_5_wind)
        st.plotly_chart(graph.scatter_plot.pm2_5_temp)
        st.plotly_chart(graph.scatter_plot.pm2_5_light)

    st.plotly_chart(graph.heatmap.envi_corr)

col1, col2 = st.columns(2)
with col1.expander("Fun Exploration: Does Earthquake affect PM 2.5?"):
    st.plotly_chart(graph.box_plot.pm2_5_earthquake)
with col2.expander("Fun Exploration: Does Songkran affect PM 2.5?"):
    st.plotly_chart(graph.box_plot.pm2_5_songkran)
