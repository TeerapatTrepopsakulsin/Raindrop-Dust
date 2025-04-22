"""Show Dataset."""
import streamlit as st
from frontend.utils.dataframe import pmr_df, snd_df, hour_df
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
        background-color: {color_4};
        color: {head_text};
    }}
    
    details > summary::-webkit-details-marker {{
        display: none;
    }}
</style>
""", unsafe_allow_html=True)

custom_cmap = mcolors.LinearSegmentedColormap.from_list(
    "white_to_blue", [head_text, color_2]
)

pri  = """
**Column Descriptions**
- ts: timestamp
- temp: Temperature (C°)
- light: Light (Lux)
- hum: Humidity (%)
- aqi: Air Quality Index
- pm1_0: PM 1.0 concentration μ g/m3 (factory environment)
- pm2_5: PM 2.5 concentration μ g/m3 (factory environment)
- pm10_0: PM 10.0 concentration μ g/m3 (factory environment)
- pm1_0_atm: PM 1.0 concentration μ g/m3 (atmospheric environment)
- pm2_5_atm: PM 2.5 concentration μ g/m3 (atmospheric environment)
- pm10_0_atm: PM 10.0 concentration μ g/m3 (atmospheric environment)
- pcnt_0_3: Particle count of diameter beyond 0.3 um in 0.1 liter or air
- pcnt_0_5: Particle count of diameter beyond 0.5 um in 0.1 liter or air
- pcnt_1_0: Particle count of diameter beyond 1.0 um in 0.1 liter or air
- pcnt_2_5: Particle count of diameter beyond 2.5 um in 0.1 liter or air
- pcnt_5_0: Particle count of diameter beyond 10.0 um in 0.1 liter or air
- pcnt_10_0: Particle count of diameter beyond 10.0 um in 0.1 liter or air
"""

sec = """
**Column Descriptions**
- ts: timestamp
- lat: Latitude
- lon: Longitude
- temp: Temperature (C°)
- hum: Humidity (%)
- weather_main: Group of weather parameters (Rain, Snow, Clouds etc.)
- weather_con: Weather condition within the group
- wind_spd: Wind speed (m/s)
- cloud: Cloudiness (%)
- rain: Precipitation (where available) (mm/h)
"""

hour = """
**Column Descriptions**
- ts: timestamp
- lat: Latitude
- lon: Longitude
- temp: Temperature (C°)
- hum: Humidity (%)
- weather_main: Group of weather parameters (Rain, Snow, Clouds etc.)
- weather_con: Weather condition within the group
- temp_max: Maximum Temperature (C°)
- temp_min: Minimum Temperature (C°)
- wind_spd: Wind speed (m/s)
- cloud: Cloudiness (%)
- rain: Precipitation (where available) (mm/h)
- light: Light (Lux)
- aqi: Air Quality Index
- pm1_0: PM 1.0 concentration μ g/m3 (factory environment)
- pm2_5: PM 2.5 concentration μ g/m3 (factory environment)
- pm10_0: PM 10.0 concentration μ g/m3 (factory environment)
- pm1_0_atm: PM 1.0 concentration μ g/m3 (atmospheric environment)
- pm2_5_atm: PM 2.5 concentration μ g/m3 (atmospheric environment)
- pm10_0_atm: PM 10.0 concentration μ g/m3 (atmospheric environment)
- pcnt_0_3: Particle count of diameter beyond 0.3 um in 0.1 liter or air
- pcnt_0_5: Particle count of diameter beyond 0.5 um in 0.1 liter or air
- pcnt_1_0: Particle count of diameter beyond 1.0 um in 0.1 liter or air
- pcnt_2_5: Particle count of diameter beyond 2.5 um in 0.1 liter or air
- pcnt_5_0: Particle count of diameter beyond 10.0 um in 0.1 liter or air
- pcnt_10_0: Particle count of diameter beyond 10.0 um in 0.1 liter or air
"""

def show_table(df, text, key_prefix=""):
    if st.toggle("❇️ Show full table (might be slow!)", value=False, key=f"{key_prefix}_toggle", help=text):
        df_to_show = df
    else:
        df_to_show = df.head(50)

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

st.markdown("<div class='main-title'>Dataset & Tables</div>", unsafe_allow_html=True)

with st.expander("Primary Table", icon="📝", expanded=True):
    show_table(pmr_df, pri, key_prefix="pmr")

with st.expander("Secondary Table", icon="💻"):
    show_table(snd_df, sec, key_prefix="snd")

with st.expander("Hourly Table", icon="⏰"):
    show_table(hour_df, hour, key_prefix="hour")
