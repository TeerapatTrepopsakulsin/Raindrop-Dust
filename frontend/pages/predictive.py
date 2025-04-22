"""Forcasting data."""
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

    .section-title {{
        font-size: 1.6em;
        font-weight: bold;
        color: {color_2};
        border-bottom: 2px solid #ecf0f1;
        padding-bottom: 5px;
        margin-top: 30px;
        margin-bottom: 10px;
    }}

    div[data-testid="stMetric"] {{
        background-color: {color_4};
        transition: background-color 0.3s ease;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }}

    div[data-testid="stMetric"]:hover {{
        background-color: {color_3};
    }}

        div[data-testid="stMetric"] > div {{
        justify-content: center;
        text-align: center;
    }}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>Air Quality Forecasting</div>", unsafe_allow_html=True)

oneday_tab, threedays_tab = st.tabs(["⏰ 24 Hours (1 day)", "📅 72 Hours (3 days)"])

with oneday_tab:
    forecast_1d = graph.stats.oneday_forecast

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("<div class='section-title'>⚖️ Average</div>", unsafe_allow_html=True)
        st.metric("AQI", f"{forecast_1d.loc['mean', 'aqi']:.2f}"
                  , border=True, help="KidBright")
        st.metric("PM 2.5 (µg/m³)", f"{forecast_1d.loc['mean', 'pm2_5']:.2f}"
                  , border=True, help="KidBright")
        st.metric("PM 10.0 (µg/m³)", f"{forecast_1d.loc['mean', 'pm10_0']:.2f}"
                  , border=True, help="KidBright")
    with col2:
        st.markdown("<div class='section-title'>🔽 Minimum</div>", unsafe_allow_html=True)
        st.metric("AQI", f"{forecast_1d.loc['min', 'aqi']:.2f}"
                    , border=True, help="KidBright")
        st.metric("PM 2.5 (µg/m³)", f"{forecast_1d.loc['min', 'pm2_5']:.2f}"
                    , border=True, help="KidBright")
        st.metric("PM 10.0 (µg/m³)", f"{forecast_1d.loc['min', 'pm10_0']:.2f}"
                    , border=True, help="KidBright")
    with col3:
        st.markdown("<div class='section-title'>🔼 Maximum</div>", unsafe_allow_html=True)
        st.metric("AQI", f"{forecast_1d.loc['max', 'aqi']:.2f}"
                    , border=True, help="KidBright")
        st.metric("PM 2.5 (µg/m³)", f"{forecast_1d.loc['max', 'pm2_5']:.2f}"
                    , border=True, help="KidBright")
        st.metric("PM 10.0 (µg/m³)", f"{forecast_1d.loc['max', 'pm10_0']:.2f}"
                    , border=True, help="KidBright")
    with col4:
        st.image("pic/air_po.jpg", use_container_width=True)

    st.markdown("<div class='section-title'>📈 Trends</div>", unsafe_allow_html=True)
    st.plotly_chart(graph.line_graph.pm_forecast1d, use_container_width=True)
    st.plotly_chart(graph.line_graph.aqi_forecast1d, use_container_width=True)

with threedays_tab:
    forecast_3d = graph.stats.threedays_forecast

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("<div class='section-title'>⚖️ Average</div>", unsafe_allow_html=True)
        st.metric("AQI", f"{forecast_3d.loc['mean', 'aqi']:.2f}"
                  , border=True, help="KidBright")
        st.metric("PM 2.5 (µg/m³)", f"{forecast_3d.loc['mean', 'pm2_5']:.2f}"
                  , border=True, help="KidBright")
        st.metric("PM 10.0 (µg/m³)", f"{forecast_3d.loc['mean', 'pm10_0']:.2f}"
                  , border=True, help="KidBright")
    with col2:
        st.markdown("<div class='section-title'>🔽 Minimum</div>", unsafe_allow_html=True)
        st.metric("AQI", f"{forecast_3d.loc['min', 'aqi']:.2f}"
                  , border=True, help="KidBright")
        st.metric("PM 2.5 (µg/m³)", f"{forecast_3d.loc['min', 'pm2_5']:.2f}"
                  , border=True, help="KidBright")
        st.metric("PM 10.0 (µg/m³)", f"{forecast_3d.loc['min', 'pm10_0']:.2f}"
                  , border=True, help="KidBright")
    with col3:
        st.markdown("<div class='section-title'>🔼 Maximum</div>", unsafe_allow_html=True)
        st.metric("AQI", f"{forecast_3d.loc['max', 'aqi']:.2f}"
                  , border=True, help="KidBright")
        st.metric("PM 2.5 (µg/m³)", f"{forecast_3d.loc['max', 'pm2_5']:.2f}"
                  , border=True, help="KidBright")
        st.metric("PM 10.0 (µg/m³)", f"{forecast_3d.loc['max', 'pm10_0']:.2f}"
                  , border=True, help="KidBright")
    with col4:
        st.image("pic/air_po.jpg", use_container_width=True)

    st.markdown("<div class='section-title'>📈 Trends</div>", unsafe_allow_html=True)
    st.plotly_chart(graph.line_graph.pm_forecast3d, use_container_width=True)
    st.plotly_chart(graph.line_graph.aqi_forecast3d, use_container_width=True)
