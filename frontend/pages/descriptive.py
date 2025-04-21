import time
import streamlit as st
from frontend.components import graph

head_text = "#ECEFCA"
color_2 = "#94B4C1"
color_3 = "#547792"
color_4 = "#213448"

st.markdown(f"""
<style>
    .main-title {{
        font-size: 3em;
        font-weight: bold;
        color: {color_2};
        margin-bottom: 0.3em;
    }}
    
    details summary {{
        font-size: 1.2em;
        font-weight: bold;
        background-color: {color_3};
        color: {head_text};
        padding: 10px;
        border-radius: 10px;
        cursor: pointer;
    }}
    
    
    details summary {{
        font-size: 1.2em;
        font-weight: bold;
        background-color: {color_3};
        color: {head_text};
        padding: 10px;
        border-radius: 10px;
        cursor: pointer;
    }}
    
    details summary:hover {{
        background-color: {head_text};
        color: {color_4};
    }}
    
    details[open] summary {{
        background-color: #213448;
    }}
    
    details > summary::-webkit-details-marker {{
        display: none;
    }}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>Descriptive Data & Statistics</div>", unsafe_allow_html=True)

st.markdown("<div class='section-title'>☁️ Weather Condition</div>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    with st.expander("Main"):
        st.plotly_chart(graph.box_plot.pm2_5_weather_main)
        st.plotly_chart(graph.bar_chart.pm_aqi_weather_main)

        s_col1, s_col2 = st.columns(2)
        s_col1.plotly_chart(graph.pie_chart.pm2_5_weather_main)
        s_col2.dataframe(graph.stats.pm_aqi_weather_main)

with col2:
    with st.expander("Detailed"):
        st.plotly_chart(graph.box_plot.pm2_5_weather_con)
        st.plotly_chart(graph.bar_chart.pm_aqi_weather_con)

        s_col1, s_col2 = st.columns(2)
        s_col1.plotly_chart(graph.pie_chart.pm2_5_weather_con)
        s_col2.dataframe(graph.stats.pm_aqi_weather_con)

with st.expander("Raindrops"):
    st.plotly_chart(graph.box_plot.pm2_5_rain)
    st.dataframe(graph.stats.pm2_5_rain)

st.markdown("<div class='section-title'>🏭 Air</div>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    with st.expander("Air Quality Trend"):
        st.plotly_chart(graph.line_graph.pm_ts)
        st.plotly_chart(graph.line_graph.aqi_ts)
with col2:
    st.image("pic/sky.jpg", use_container_width=True)

with st.expander("Distributions"):
    st.plotly_chart(graph.histogram.pm2_5)
    st.plotly_chart(graph.histogram.pm10_0)
    st.plotly_chart(graph.histogram.aqi)

st.markdown("<div class='section-title'>➕ Others</div>", unsafe_allow_html=True)
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

st.markdown("<div class='section-title'>💡 Fun Exploration</div>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1.expander("Does Earthquake affect PM 2.5?"):
    st.plotly_chart(graph.box_plot.pm2_5_earthquake)
with col2.expander("Does Songkran affect PM 2.5?"):
    st.plotly_chart(graph.box_plot.pm2_5_songkran)
