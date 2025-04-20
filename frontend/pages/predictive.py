import streamlit as st
from frontend.components import graph


st.header("Air Quality Forecasting")

oneday_tab, threedays_tab = st.tabs(["24 Hours", "72 Hours"])

# Visualise
with oneday_tab:
    st.subheader("24 Hours Forecast")

    st.plotly_chart(graph.line_graph.pm_forecast1d)

    st.plotly_chart(graph.line_graph.aqi_forecast1d)

    forecast_1d = graph.stats.oneday_forecast

    # Mean
    col1, col2, col3 = st.columns(3)
    col1.metric("Average AQI", f"{forecast_1d.loc['mean', 'aqi']:.2f}")
    col2.metric("Average PM 2.5", f"{forecast_1d.loc['mean', 'pm2_5']:.2f} µg/m³")
    col3.metric("Average PM 10", f"{forecast_1d.loc['mean', 'pm10_0']:.2f} µg/m³")

    # Min
    col1, col2, col3 = st.columns(3)
    col1.metric("Minimum AQI", f"{forecast_1d.loc['min', 'aqi']:.2f}")
    col2.metric("Minimum PM 2.5", f"{forecast_1d.loc['min', 'pm2_5']:.2f} µg/m³")
    col3.metric("Minimum PM 10", f"{forecast_1d.loc['min', 'pm10_0']:.2f} µg/m³")

    # Max
    col1, col2, col3 = st.columns(3)
    col1.metric("Maximum AQI", f"{forecast_1d.loc['max', 'aqi']:.2f}")
    col2.metric("Maximum PM 2.5", f"{forecast_1d.loc['max', 'pm2_5']:.2f} µg/m³")
    col3.metric("Maximum PM 10", f"{forecast_1d.loc['max', 'pm10_0']:.2f} µg/m³")

with threedays_tab:

    st.subheader("72 Hours Forecast")

    st.plotly_chart(graph.line_graph.pm_forecast3d)

    st.plotly_chart(graph.line_graph.aqi_forecast3d)

    forecast_3d = graph.stats.threedays_forecast

    # Mean
    col1, col2, col3 = st.columns(3)
    col1.metric("Average AQI", f"{forecast_3d.loc['mean', 'aqi']:.2f}")
    col2.metric("Average PM 2.5", f"{forecast_3d.loc['mean', 'pm2_5']:.2f} µg/m³")
    col3.metric("Average PM 10", f"{forecast_3d.loc['mean', 'pm10_0']:.2f} µg/m³")

    # Min
    col1, col2, col3 = st.columns(3)
    col1.metric("Minimum AQI", f"{forecast_3d.loc['min', 'aqi']:.2f}")
    col2.metric("Minimum PM 2.5", f"{forecast_3d.loc['min', 'pm2_5']:.2f} µg/m³")
    col3.metric("Minimum PM 10", f"{forecast_3d.loc['min', 'pm10_0']:.2f} µg/m³")

    # Max
    col1, col2, col3 = st.columns(3)
    col1.metric("Maximum AQI", f"{forecast_3d.loc['max', 'aqi']:.2f}")
    col2.metric("Maximum PM 2.5", f"{forecast_3d.loc['max', 'pm2_5']:.2f} µg/m³")
    col3.metric("Maximum PM 10", f"{forecast_3d.loc['max', 'pm10_0']:.2f} µg/m³")
