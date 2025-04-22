"""Show current/latest/recent data."""
import streamlit as st
from frontend.components import graph
import matplotlib.colors as mcolors

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
        padding: 1rem;
        margin: 5px;
        border-radius: 10px;
        backdrop-filter: blur(5px);
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

custom_cmap = mcolors.LinearSegmentedColormap.from_list(
    "white_to_blue", [head_text, color_2]
)

st.markdown("<div class='main-title'>Current Condition</div>", unsafe_allow_html=True)

latest_tab, today_tab, week_tab = st.tabs(["📍 Latest", "⏰ Today", "📅 This Week"])

with latest_tab:
    latest_df = graph.stats.latest
    delta_df = graph.stats.delta

    st.markdown(
        f"<span style='color: {color_3}; font-weight: bold;'>Update: {latest_df['ts']}</span>",
        unsafe_allow_html=True
    )

    st.markdown("<div class='section-title'>☁️ Weather Overview</div>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Cloud (%)", f"{latest_df['cloud']:.2f}", f"{delta_df['cloud']:.2f}"
                , border=True, help="OpenWeatherAPI")
    col2.metric("Total Rainfall (mm)", f"{latest_df['rain']:.2f}", f"{delta_df['rain']:.2f}"
                , border=True, help="OpenWeatherAPI")
    col3.metric("Wind speed (m/s)", f"{latest_df['wind_spd']:.2f}", f"{delta_df['wind_spd']:.2f}"
                , border=True, help="OpenWeatherAPI")
    col4.metric("Weather condition", f"{latest_df['weather_main']}", f"{latest_df['weather_con']}",
                delta_color="off", border=True, help="OpenWeatherAPI")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='section-title'>💧 Environment</div>", unsafe_allow_html=True)
        st.metric("Humidity (%)", f"{latest_df['hum']:.2f}", f"{delta_df['hum']:.2f}"
                  , border=True, help="KidBright")
        st.metric("Light (lux)", f"{latest_df['light']:.2f}", f"{delta_df['light']:.2f}"
                  , border=True, help="KidBright")
        st.metric("Air Quality Index", f"{latest_df['aqi']:.2f}", f"{delta_df['aqi']:.2f}"
                  , border=True, help="KidBright")
    with col2:
        st.markdown("<div class='section-title'>🌡️ Temperature</div>", unsafe_allow_html=True)
        st.metric("Average temperature (°C)", f"{latest_df['temp']:.2f}", f"{delta_df['temp']:.2f}"
                  , border=True, help="KidBright")
        st.metric("Minimum temperature (°C)", f"{latest_df['min_temp']:.2f}", f"{delta_df['min_temp']:.2f}"
                  , border=True, help="KidBright")
        st.metric("Maximum temperature (°C)", f"{latest_df['max_temp']:.2f}", f"{delta_df['max_temp']:.2f}"
                  , border=True, help="KidBright")
    with col3:
        st.image("pic/sky.jpg", use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='section-title'>🌀 PM: Atmospheric</div>", unsafe_allow_html=True)
        st.metric("PM 1.0 (µg/m³)", f"{latest_df['pm1_0_atm']:.2f}", f"{delta_df['pm1_0_atm']:.2f}"
                  , border=True, help="KidBright")
        st.metric("PM 2.5 (µg/m³)", f"{latest_df['pm2_5_atm']:.2f}", f"{delta_df['pm2_5_atm']:.2f}"
                  , border=True, help="KidBright")
        st.metric("PM 10.0 (µg/m³)", f"{latest_df['pm10_0_atm']:.2f}", f"{delta_df['pm10_0_atm']:.2f}"
                  , border=True, help="KidBright")
    with col2:
        st.markdown("<div class='section-title'>🏭 PM: Factory Sensor</div>", unsafe_allow_html=True)
        st.metric("PM 1.0 (µg/m³)", f"{latest_df['pm1_0']:.2f}³", f"{delta_df['pm1_0']:.2f}"
                  , border=True, help="KidBright")
        st.metric("PM 2.5 (µg/m³)", f"{latest_df['pm2_5']:.2f}", f"{delta_df['pm2_5']:.2f}"
                  , border=True, help="KidBright")
        st.metric("PM 10.0 (µg/m³)", f"{latest_df['pm10_0']:.2f}", f"{delta_df['pm10_0']:.2f}"
                  , border=True, help="KidBright")

    st.markdown("<div class='section-title'>🧪 Particle Count</div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Particles > 0.3 μm", f"{latest_df['pcnt_0_3']:.2f}", f"{delta_df['pcnt_0_3']:.2f}"
                  , border=True, help="KidBright")
        st.metric("Particles > 0.5 μm", f"{latest_df['pcnt_0_5']:.2f}", f"{delta_df['pcnt_0_5']:.2f}"
                  , border=True, help="KidBright")
    with col2:
        st.metric("Particles > 1.0 μm", f"{latest_df['pcnt_1_0']:.2f}", f"{delta_df['pcnt_1_0']:.2f}"
                  , border=True, help="KidBright")
        st.metric("Particles > 2.5 μm", f"{latest_df['pcnt_2_5']:.2f}", f"{delta_df['pcnt_2_5']:.2f}"
                  , border=True, help="KidBright")
    with col3:
        st.metric("Particles > 5 μm", f"{latest_df['pcnt_5_0']:.2f}", f"{delta_df['pcnt_5_0']:.2f}"
                  , border=True, help="KidBright")
        st.metric("Particles > 10 μm", f"{latest_df['pcnt_10_0']:.2f}", f"{delta_df['pcnt_10_0']:.2f}"
                  , border=True, help="KidBright")

with today_tab:
    st.markdown("<div class='section-title'>📊 Today's Descriptive Statistics</div>", unsafe_allow_html=True)

    st.dataframe(graph.stats.today.style.background_gradient(
        cmap=custom_cmap, axis=0
    ).set_properties(
        **{
            'color': color_4,
            'font-weight': 'bold'
        }
    ).format("{:.2f}"), use_container_width=True)

    st.plotly_chart(graph.line_graph.aqi_ts_today, use_container_width=True)
    st.plotly_chart(graph.line_graph.pm_ts_today, use_container_width=True)

with week_tab:
    st.markdown("<div class='section-title'>📊 This Week's Descriptive Statistics</div>", unsafe_allow_html=True)

    st.dataframe(graph.stats.week.style.background_gradient(
        cmap=custom_cmap, axis=0
    ).set_properties(
        **{
            'color': color_4,
            'font-weight': 'bold'
        }
    ).format("{:.2f}"), use_container_width=True)

    st.plotly_chart(graph.line_graph.aqi_ts_week, use_container_width=True)
    st.plotly_chart(graph.line_graph.pm_ts_week, use_container_width=True)
