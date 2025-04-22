"""Descriptive data storytelling and correlations."""
import time
import streamlit as st
from frontend.components import graph
import matplotlib.colors as mcolors
import numpy as np

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
    
    .section-title {{
        font-size: 1.6em;
        font-weight: bold;
        color: {color_2};
        border-bottom: 2px solid #ecf0f1;
        padding-bottom: 5px;
        margin-top: 30px;
        margin-bottom: 10px;
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

custom_cmap = mcolors.LinearSegmentedColormap.from_list(
    "white_to_blue", [head_text, color_2]
)

def show_table(df):
    df_to_show = df

    numeric_cols = df_to_show.select_dtypes(include=np.number).columns
    non_numeric_cols = df_to_show.select_dtypes(exclude=np.number).columns

    styled_df = df_to_show.style

    styled_df = styled_df.background_gradient(
        cmap=custom_cmap,
        axis=0,
        subset=numeric_cols
    ).format(
        "{:.2f}",
        subset=numeric_cols
    ).set_properties(
        **{
            'color': color_4,
            'font-weight': 'bold'
        },
        subset=numeric_cols
    )

    styled_df = styled_df.set_properties(
        **{
            'color': head_text,
            'font-weight': 'bold'
        },
        subset=non_numeric_cols
    )

    st.dataframe(styled_df, use_container_width=True)

st.markdown("<div class='main-title'>Descriptive Data & Statistics</div>", unsafe_allow_html=True)

st.markdown("<div class='section-title'>☁️ Weather Condition</div>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    with st.expander("Main"):
        st.plotly_chart(graph.box_plot.pm2_5_weather_main)
        st.plotly_chart(graph.bar_chart.pm_aqi_weather_main)

        s_col1, s_col2 = st.columns(2)
        with s_col1:
            st.plotly_chart(graph.pie_chart.pm2_5_weather_main)
        with s_col2:
            show_table(graph.stats.pm_aqi_weather_main)

with col2:
    with st.expander("Detailed"):
        st.plotly_chart(graph.box_plot.pm2_5_weather_con)
        st.plotly_chart(graph.bar_chart.pm_aqi_weather_con)

        s_col1, s_col2 = st.columns(2)
        with s_col1:
            st.plotly_chart(graph.pie_chart.pm2_5_weather_con)
        with s_col2:
            show_table(graph.stats.pm_aqi_weather_con)

with st.expander("Raindrops"):
    st.plotly_chart(graph.box_plot.pm2_5_rain)
    show_table(graph.stats.pm2_5_rain)

st.markdown("<div class='section-title'>🏭 Air</div>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    with st.expander("Air Quality Trend"):
        st.plotly_chart(graph.line_graph.pm_ts)
        st.plotly_chart(graph.line_graph.aqi_ts)
with col2:
    with st.expander("Distributions"):
        st.plotly_chart(graph.histogram.pm2_5)
        st.plotly_chart(graph.histogram.pm10_0)
        st.plotly_chart(graph.histogram.aqi)

st.markdown("<div class='section-title'>➕ Others</div>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    with st.expander("Day of Week"):
        st.plotly_chart(graph.box_plot.pm2_5_day_of_week)
        st.plotly_chart(graph.bar_chart.pm_aqi_day_of_week)

        s_col1, s_col2 = st.columns(2)
        with s_col1:
            st.plotly_chart(graph.pie_chart.pm2_5_day_of_week)
        with s_col2:
            show_table(graph.stats.pm_aqi_day_of_week)

with col2:
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
