import streamlit as st
from frontend.components import graph


st.header("Current Condition")

# Create tabs for Today and This Week
latest_tab, today_tab, week_tab = st.tabs(["Latest", "Today", "This Week"])

with latest_tab:
    latest_df = graph.stats.latest
    delta_df = graph.stats.delta

    st.markdown(
        f"<span style='color: #1f77b4; font-weight: bold;'>Update: {latest_df['ts']}</span>",
        unsafe_allow_html=True
    )

    # Row 1
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Cloud", f"{latest_df['cloud']:.2f} %", f"{delta_df['cloud']:.2f}", delta_color="inverse")
    col2.metric("Total Rainfall", f"{latest_df['rain']:.2f} mm", f"{delta_df['rain']:.2f}", delta_color="inverse")
    col3.metric("Wind speed", f"{latest_df['wind_spd']:.2f} m/s", f"{delta_df['wind_spd']:.2f}",
                delta_color="inverse")
    col4.metric("Weather condition", f"{latest_df['weather_main']}", f"{latest_df['weather_con']}",
                delta_color="off")

    # Row 2
    col1, col2, col3 = st.columns(3)
    col1.metric("Average temperature", f"{latest_df['temp_pmr']:.2f} °C",
                f"{delta_df['temp_pmr']:.2f}", delta_color="inverse")
    col2.metric("Minimum temperature", f"{latest_df['min_temp']:.2f} °C",
                f"{delta_df['min_temp']:.2f}", delta_color="inverse")
    col3.metric("Maximum temperature", f"{latest_df['max_temp']:.2f} °C",
                f"{delta_df['max_temp']:.2f}", delta_color="inverse")

    # Row 3
    col1, col2, col3 = st.columns(3)
    col1.metric("Humidity", f"{latest_df['hum_pmr']:.2f} %", f"{delta_df['hum_pmr']:.2f}", delta_color="inverse")
    col2.metric("Light", f"{latest_df['light']:.2f} lux", f"{delta_df['light']:.2f}", delta_color="inverse")
    col3.metric("Air Quality Index", f"{latest_df['aqi']:.2f}", f"{delta_df['aqi']:.2f}", delta_color="inverse")

    # Row 4
    col1, col2, col3 = st.columns(3)
    col1.metric("PM 1.0 (Atmospheric)", f"{latest_df['pm1_0_atm']:.2f} µg/m³", f"{delta_df['pm1_0_atm']:.2f}", delta_color="inverse")
    col2.metric("PM 2.5 (Atmospheric)", f"{latest_df['pm2_5_atm']:.2f} µg/m³", f"{delta_df['pm2_5_atm']:.2f}", delta_color="inverse")
    col3.metric("PM 10 (Atmospheric)", f"{latest_df['pm10_0_atm']:.2f} µg/m³", f"{delta_df['pm10_0_atm']:.2f}", delta_color="inverse")

    # Row 5
    col1, col2, col3 = st.columns(3)
    col1.metric("PM 1.0 (Factory)", f"{latest_df['pm1_0']:.2f} µg/m³", f"{delta_df['pm1_0']:.2f}", delta_color="inverse")
    col2.metric("PM 2.5 (Factory)", f"{latest_df['pm2_5']:.2f} µg/m³", f"{delta_df['pm2_5']:.2f}", delta_color="inverse")
    col3.metric("PM 10 (Factory)", f"{latest_df['pm10_0']:.2f} µg/m³", f"{delta_df['pm10_0']:.2f}", delta_color="inverse")

    # Row 6
    col1, col2, col3 = st.columns(3)
    col1.metric("Particles > 0.3 μm", f"{latest_df['pcnt_0_3']:.2f}", f"{delta_df['pcnt_0_3']:.2f}",
                delta_color="inverse")
    col2.metric("Particles > 0.5 μm", f"{latest_df['pcnt_0_5']:.2f}", f"{delta_df['pcnt_0_5']:.2f}",
                delta_color="inverse")
    col3.metric("Particles > 1.0 μm", f"{latest_df['pcnt_1_0']:.2f}", f"{delta_df['pcnt_1_0']:.2f}",
                delta_color="inverse")

    # Row 7
    col1, col2, col3 = st.columns(3)
    col1.metric("Particles > 2.5 μm", f"{latest_df['pcnt_2_5']:.2f}", f"{delta_df['pcnt_2_5']:.2f}",
                delta_color="inverse")
    col2.metric("Particles > 5 μm", f"{latest_df['pcnt_5_0']:.2f}", f"{delta_df['pcnt_5_0']:.2f}",
                delta_color="inverse")
    col3.metric("Particles > 10 μm", f"{latest_df['pcnt_10_0']:.2f}", f"{delta_df['pcnt_10_0']:.2f}",
                delta_color="inverse")

with today_tab:
    st.subheader("Today's Statistics")

    st.plotly_chart(graph.line_graph.aqi_ts_today, use_container_width=True)
    st.plotly_chart(graph.line_graph.pm_ts_today, use_container_width=True)

    st.text("Descriptive Statistics")
    st.dataframe(graph.stats.today)

with week_tab:
    st.subheader("This Week's Statistics")

    st.plotly_chart(graph.line_graph.aqi_ts_week, use_container_width=True)
    st.plotly_chart(graph.line_graph.pm_ts_week, use_container_width=True)

    st.text("Descriptive Statistics")
    st.dataframe(graph.stats.week)
