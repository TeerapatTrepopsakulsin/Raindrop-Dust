import streamlit as st
from frontend.components import graph
from streamlit_extras.metric_cards import style_metric_cards

head_text = "#ECEFCA"
color_2 = "#94B4C1"
color_3 = "#054d0c"
color_4 = "#1abc9c"
red = "#e74c3c"
green = "#e74c3c"
grey = "#7f8c8d"

st.markdown(f"""
<style>
    .main-title {{
        font-size: 3em;
        font-weight: 700;
        color: {head_text};
        margin-bottom: 0.3em;
    }}

    .section-title {{
        font-size: 1.6em;
        font-weight: 600;
        color: {color_2};
        border-bottom: 2px solid #ecf0f1;
        padding-bottom: 5px;
        margin-top: 30px;
        margin-bottom: 10px;
    }}
</style>
""", unsafe_allow_html=True)

style_metric_cards(
    background_color="#547792",
    border_color=head_text,
    border_left_color=head_text
)

st.markdown("<div class='main-title'>Current Condition</div>", unsafe_allow_html=True)

latest_tab, today_tab, week_tab = st.tabs(["📍 Latest", "📅 Today", "📈 This Week"])

with latest_tab:
    latest_df = graph.stats.latest
    delta_df = graph.stats.delta

    st.markdown(
        f"<span style='color: #1f77b4; font-weight: bold;'>Update: {latest_df['ts']}</span>",
        unsafe_allow_html=True
    )

    st.markdown("<div class='section-title'>☁️ Weather Overview</div>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Cloud", f"{latest_df['cloud']:.2f} %", f"{delta_df['cloud']:.2f}", delta_color="inverse")
    col2.metric("Total Rainfall", f"{latest_df['rain']:.2f} mm", f"{delta_df['rain']:.2f}", delta_color="inverse")
    col3.metric("Wind speed", f"{latest_df['wind_spd']:.2f} m/s", f"{delta_df['wind_spd']:.2f}",
              delta_color="inverse")
    col4.metric("Weather condition", f"{latest_df['weather_main']}", f"{latest_df['weather_con']}",
              delta_color="off")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='section-title'>💧 Environment</div>", unsafe_allow_html=True)
        st.metric("Humidity", f"{latest_df['hum']:.2f} %", f"{delta_df['hum']:.2f}", delta_color="inverse")
        st.metric("Light", f"{latest_df['light']:.2f} lux", f"{delta_df['light']:.2f}", delta_color="inverse")
        st.metric("Air Quality Index", f"{latest_df['aqi']:.2f}", f"{delta_df['aqi']:.2f}", delta_color="inverse")
    with col2:
        st.markdown("<div class='section-title'>🌡️ Temperature</div>", unsafe_allow_html=True)
        st.metric("Average temperature", f"{latest_df['temp']:.2f} °C",
                    f"{delta_df['temp']:.2f}", delta_color="inverse")
        st.metric("Minimum temperature", f"{latest_df['min_temp']:.2f} °C",
                    f"{delta_df['min_temp']:.2f}", delta_color="inverse")
        st.metric("Maximum temperature", f"{latest_df['max_temp']:.2f} °C",
                    f"{delta_df['max_temp']:.2f}", delta_color="inverse")

    st.markdown("<div class='section-title'>PM</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='section-title'>🌫️ Atmospheric</div>", unsafe_allow_html=True)
        st.metric("PM 1.0", f"{latest_df['pm1_0_atm']:.2f} µg/m³", f"{delta_df['pm1_0_atm']:.2f}",
                    delta_color="inverse")
        st.metric("PM 2.5", f"{latest_df['pm2_5_atm']:.2f} µg/m³", f"{delta_df['pm2_5_atm']:.2f}",
                    delta_color="inverse")
        st.metric("PM 10.0", f"{latest_df['pm10_0_atm']:.2f} µg/m³", f"{delta_df['pm10_0_atm']:.2f}",
                    delta_color="inverse")
    with col2:
        st.markdown("<div class='section-title'>🏭 Factory Sensor</div>", unsafe_allow_html=True)
        st.metric("PM 1.0", f"{latest_df['pm1_0']:.2f} µg/m³", f"{delta_df['pm1_0']:.2f}",
                    delta_color="inverse")
        st.metric("PM 2.5", f"{latest_df['pm2_5']:.2f} µg/m³", f"{delta_df['pm2_5']:.2f}",
                    delta_color="inverse")
        st.metric("PM 10.0", f"{latest_df['pm10_0']:.2f} µg/m³", f"{delta_df['pm10_0']:.2f}",
                    delta_color="inverse")

    st.markdown("<div class='section-title'>🧪 Particle Count</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Particles > 0.3 μm", f"{latest_df['pcnt_0_3']:.2f}", f"{delta_df['pcnt_0_3']:.2f}",
                    delta_color="inverse")
        st.metric("Particles > 0.5 μm", f"{latest_df['pcnt_0_5']:.2f}", f"{delta_df['pcnt_0_5']:.2f}",
                    delta_color="inverse")
        st.metric("Particles > 1.0 μm", f"{latest_df['pcnt_1_0']:.2f}", f"{delta_df['pcnt_1_0']:.2f}",
                    delta_color="inverse")
    with col2:
        st.metric("Particles > 2.5 μm", f"{latest_df['pcnt_2_5']:.2f}", f"{delta_df['pcnt_2_5']:.2f}",
                    delta_color="inverse")
        st.metric("Particles > 5 μm", f"{latest_df['pcnt_5_0']:.2f}", f"{delta_df['pcnt_5_0']:.2f}",
                    delta_color="inverse")
        st.metric("Particles > 10 μm", f"{latest_df['pcnt_10_0']:.2f}", f"{delta_df['pcnt_10_0']:.2f}",
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