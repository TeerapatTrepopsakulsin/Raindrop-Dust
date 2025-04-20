import streamlit as st
from frontend.components import graph

head_text = "#ECEFCA"
color_2 = "#4d5e34"
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

    .metric-box {{
        background: {color_3};
        padding: 1em;
        border-radius: 14px;
        color: white;
        margin-bottom: 1em;
        text-align: center;
        transition: background-color 0.3s ease;
    }}
    
        .metric-box:hover {{
        background: {color_4};
    }}

    [data-testid="stMetric"] {{
        background: none;
        padding: 0 !important;
        margin: 0 !important;
    }}

    .element-container:has([data-testid="stMetric"]) {{
        margin-top: -8px;
    }}
</style>
""", unsafe_allow_html=True)


def render_metric_row(metrics, cols=3, title="aaa"):
    with st.expander(title, expanded=False):
        columns = st.columns(cols)
        for col, metric in zip(columns, metrics):
            with col:
                label = metric.get("label", "")
                value = metric.get("value", "")
                delta = metric.get("delta", "")
                delta_color = metric.get("delta_color", "normal")

                delta_symbol = "↑" if "-" not in delta else "↓"
                delta_color_map = {
                    "normal": "#3498db",
                    "inverse": red if "-" not in delta else green,
                    "off": grey
                }
                color = delta_color_map.get(delta_color, "#3498db")

                st.markdown(f"""
                <div class="metric-box" style="text-align:center;">
                    <div style="font-size: 0.9em; font-weight: 600;">{label}</div>
                    <div style="font-size: 2em; font-weight: 700; margin: 0.2em 0;">{value}</div>
                    <div style="font-size: 1em; color: {color};">{delta_symbol} {delta}</div>
                </div>
                """, unsafe_allow_html=True)


st.markdown("<div class='main-title'>Current Condition</div>", unsafe_allow_html=True)

latest_tab, today_tab, week_tab = st.tabs(["📍 Latest", "📅 Today", "📈 This Week"])

with latest_tab:
    latest_df = graph.stats.latest
    delta_df = graph.stats.delta

    st.markdown(f"<span style='color: #1abc9c; font-size: 1.1em;'>🕒 Last Update: {latest_df['ts']}</span>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        # Weather
        st.markdown("<div class='section-title'>☁️ Weather Overview</div>", unsafe_allow_html=True)
        render_metric_row([
            {"label": "Cloud", "value": f"{latest_df['cloud']:.2f} %", "delta": f"{delta_df['cloud']:.2f}", "delta_color": "inverse"},
            {"label": "Rainfall", "value": f"{latest_df['rain']:.2f} mm", "delta": f"{delta_df['rain']:.2f}", "delta_color": "inverse"},
            {"label": "Wind Speed", "value": f"{latest_df['wind_spd']:.2f} m/s", "delta": f"{delta_df['wind_spd']:.2f}", "delta_color": "inverse"},
            {"label": "Weather condition", "value": latest_df['weather_main'], "delta": latest_df['weather_con'], "delta_color": "off"},
        ], cols=4, title="☁️ Weather Overview")

    with col2:
        # Temperature
        st.markdown("<div class='section-title'>🌡️ Temperature</div>", unsafe_allow_html=True)
        render_metric_row([
            {"label": "Average temperature", "value": f"{latest_df['temp']:.2f} °C", "delta": f"{delta_df['temp']:.2f}", "delta_color": "inverse"},
            {"label": "Minimum temperature", "value": f"{latest_df['min_temp']:.2f} °C", "delta": f"{delta_df['min_temp']:.2f}", "delta_color": "inverse"},
            {"label": "Maximum temperature", "value": f"{latest_df['max_temp']:.2f} °C", "delta": f"{delta_df['max_temp']:.2f}", "delta_color": "inverse"},
        ])

    # Environment
    st.markdown("<div class='section-title'>💧 Environment</div>", unsafe_allow_html=True)
    render_metric_row([
        {"label": "Humidity", "value": f"{latest_df['hum']:.2f} %", "delta": f"{delta_df['hum']:.2f}", "delta_color": "inverse"},
        {"label": "Light", "value": f"{latest_df['light']:.2f} lux", "delta": f"{delta_df['light']:.2f}", "delta_color": "inverse"},
        {"label": "Air Quality Index", "value": f"{latest_df['aqi']:.2f}", "delta": f"{delta_df['aqi']:.2f}", "delta_color": "inverse"},
    ])

    col1, col2, col3 = st.columns(2)

    with col1:
        # PM Atmospheric
        st.markdown("<div class='section-title'>🌫️ PM: Atmospheric</div>", unsafe_allow_html=True)
        render_metric_row([
            {"label": "PM 1.0", "value": f"{latest_df['pm1_0_atm']:.2f} µg/m³", "delta": f"{delta_df['pm1_0_atm']:.2f}", "delta_color": "inverse"},
            {"label": "PM 2.5", "value": f"{latest_df['pm2_5_atm']:.2f} µg/m³", "delta": f"{delta_df['pm2_5_atm']:.2f}", "delta_color": "inverse"},
            {"label": "PM 10.0", "value": f"{latest_df['pm10_0_atm']:.2f} µg/m³", "delta": f"{delta_df['pm10_0_atm']:.2f}", "delta_color": "inverse"},
        ])

    with col2:
        # PM Factory
        st.markdown("<div class='section-title'>🏭 PM: Factory Sensor</div>", unsafe_allow_html=True)
        render_metric_row([
            {"label": "PM 1.0", "value": f"{latest_df['pm1_0']:.2f} µg/m³", "delta": f"{delta_df['pm1_0']:.2f}", "delta_color": "inverse"},
            {"label": "PM 2.5", "value": f"{latest_df['pm2_5']:.2f} µg/m³", "delta": f"{delta_df['pm2_5']:.2f}", "delta_color": "inverse"},
            {"label": "PM 10.0", "value": f"{latest_df['pm10_0']:.2f} µg/m³", "delta": f"{delta_df['pm10_0']:.2f}", "delta_color": "inverse"},
        ])

    col1, col2 = st.columns(2)
    # Particle Count
    st.markdown("<div class='section-title'>🧪 Particle Count</div>", unsafe_allow_html=True)
    with col1:
        render_metric_row([
            {"label": "> 0.3 μm", "value": f"{latest_df['pcnt_0_3']:.2f}", "delta": f"{delta_df['pcnt_0_3']:.2f}",
             "delta_color": "inverse"},
            {"label": "> 0.5 μm", "value": f"{latest_df['pcnt_0_5']:.2f}", "delta": f"{delta_df['pcnt_0_5']:.2f}",
             "delta_color": "inverse"},
            {"label": "> 1.0 μm", "value": f"{latest_df['pcnt_1_0']:.2f}", "delta": f"{delta_df['pcnt_1_0']:.2f}",
             "delta_color": "inverse"},
        ])
    with col2:
        render_metric_row([
            {"label": "> 2.5 μm", "value": f"{latest_df['pcnt_2_5']:.2f}", "delta": f"{delta_df['pcnt_2_5']:.2f}",
             "delta_color": "inverse"},
            {"label": "> 5.0 μm", "value": f"{latest_df['pcnt_5_0']:.2f}", "delta": f"{delta_df['pcnt_5_0']:.2f}",
             "delta_color": "inverse"},
            {"label": "> 10.0 μm", "value": f"{latest_df['pcnt_10_0']:.2f}", "delta": f"{delta_df['pcnt_10_0']:.2f}",
             "delta_color": "inverse"},
        ])

with today_tab:
    st.markdown("<div class='section-title'>📅 Today's Statistics</div>", unsafe_allow_html=True)
    st.plotly_chart(graph.line_graph.aqi_ts_today, use_container_width=True)
    st.plotly_chart(graph.line_graph.pm_ts_today, use_container_width=True)
    st.dataframe(graph.stats.today, use_container_width=True)

with week_tab:
    st.markdown("<div class='section-title'>📈 Weekly Trends</div>", unsafe_allow_html=True)
    st.plotly_chart(graph.line_graph.aqi_ts_week, use_container_width=True)
    st.plotly_chart(graph.line_graph.pm_ts_week, use_container_width=True)
    st.dataframe(graph.stats.week, use_container_width=True)