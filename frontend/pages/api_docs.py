import streamlit as st

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
    .parameter-text {{
        color: {color_2}; 
        font-weight: bold;
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

def parameter_head():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("<div class='parameter-text'>Parameter</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='parameter-text'>Format</div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='parameter-text'>Default</div>", unsafe_allow_html=True)
    with col4:
        st.markdown("<div class='parameter-text'>Description</div>", unsafe_allow_html=True)


def parameter_data():
    parameter_head()

    with st.container(border=True):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.write("start_date")
        with col2:
            st.write("YYYY-MM-DD")
        with col3:
            st.write("The oldest date of the data")
        with col4:
            st.write("Determine the start date of the data returned (inclusive)")

    with st.container(border=True):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.write("end_date")
        with col2:
            st.write("YYYY-MM-DD")
        with col3:
            st.write("Today's date")
        with col4:
            st.write("Determine the end date of the data returned (exclusive)")

    with st.container(border=True):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.write("skip")
        with col2:
            st.write("Integer")
        with col3:
            st.write(0)
        with col4:
            st.write("Determine the number of the data to skip")

    with st.container(border=True):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.write("limit")
        with col2:
            st.write("Integer")
        with col3:
            st.write(1)
        with col4:
            st.write("Determine the number of the data returned")

def parameter_forecast():
    parameter_head()
    with st.container(border=True):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.write("limit")
        with col2:
            st.write("Integer")
        with col3:
            st.write(-1)
        with col4:
            st.write("Determine the number of the data returned")

def parameter_raw():
    parameter_head()
    with st.container(border=True):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.write("limit")
        with col2:
            st.write("Integer")
        with col3:
            st.write(-1)
        with col4:
            st.write("Determine the number of the data returned")
    with st.container(border=True):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.write("sort")
        with col2:
            st.write("Integer")
        with col3:
            st.write(0)
        with col4:
            st.write("Determine the order of the data returned (sort == 0: from the oldest to latest, "
                     "sort == 1: from the latest to oldest)")

st.markdown("<div class='main-title'>API Documentation</div>", unsafe_allow_html=True)
st.write("limit = -1: show all data")

data_tab, forcast_tab, raw_tab = st.tabs(["🗂️ Data", "✨ Forecast", "🗃️ Raw"])

with data_tab:

    st.markdown("<div class='section-title'>/data/latest</div>", unsafe_allow_html=True)
    st.markdown("<div class='parameter-text'>Get the latest data</div>", unsafe_allow_html=True)
    st.code("/data/latest?limit={limit}", language="python")
    parameter_head()
    with st.container(border=True):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.write("limit")
        with col2:
            st.write("Integer")
        with col3:
            st.write(1)
        with col4:
            st.write("Determine the number of the data returned")
    with st.expander("/data/latest"):
        st.json(
            [
                {
                    "aqi": "Air Quality Index",
                    "cloud": "Cloud, %",
                    "coordinates": {
                        "lat": "Latitude",
                        "lon": "Longitude"
                    },
                    "humidity": "Humidity, %",
                    "light": "Light level, Lux",
                    "particles_count": {
                        "description": "Particle count in 0.1 liter or air",
                        "pcnt_0_3": "Diameter beyond 0.3 um",
                        "pcnt_0_5": "Diameter beyond 0.5 um",
                        "pcnt_10_0": "Diameter beyond 10 um",
                        "pcnt_1_0": "Diameter beyond 1 um",
                        "pcnt_2_5": "Diameter beyond 2.5 um",
                        "pcnt_5_0": "Diameter beyond 5 um"
                    },
                    "pm_atmospheric": {
                        "description": "Particulate Matter concentration μg/m3 (atmospheric environment)",
                        "pm10_0": "PM 10",
                        "pm1_0": "PM 1.0",
                        "pm2_5": "PM 2.5"
                    },
                    "pm_factory": {
                        "description": "Particulate Matter concentration μg/m3 (factory environment)",
                        "pm10_0": "PM 10",
                        "pm1_0": "PM 1.0",
                        "pm2_5": "PM 2.5"
                    },
                    "rain": "Total Rainfall, mm",
                    "temp": {
                        "average": "Average temperature within the hour interval",
                        "max": "Maximum temperature within the hour interval",
                        "min": "Minimum temperature within the hour interval"
                    },
                    "timestamp": "Timestamp",
                    "weather": {
                        "description": "Descriptive weather condition",
                        "main_condition": "Vague weather condition"
                    },
                    "wind_spd": "Wind speed, m/s"
                }
            ]
        )

    st.markdown("<div class='section-title'>/data</div>", unsafe_allow_html=True)
    st.markdown("<div class='parameter-text'>Get the data</div>", unsafe_allow_html=True)
    st.code("/data?start_date={start_date}&end_date={end_date}&skip={skip}&limit={limit}", language="python")
    parameter_data()
    with st.expander("/data"):
        st.json(
            [
                {
                    "aqi": "Air Quality Index",
                    "cloud": "Cloud, %",
                    "coordinates": {
                        "lat": "Latitude",
                        "lon": "Longitude"
                    },
                    "humidity": "Humidity, %",
                    "light": "Light level, Lux",
                    "particles_count": {
                        "description": "Particle count in 0.1 liter or air",
                        "pcnt_0_3": "Diameter beyond 0.3 um",
                        "pcnt_0_5": "Diameter beyond 0.5 um",
                        "pcnt_10_0": "Diameter beyond 10 um",
                        "pcnt_1_0": "Diameter beyond 1 um",
                        "pcnt_2_5": "Diameter beyond 2.5 um",
                        "pcnt_5_0": "Diameter beyond 5 um"
                    },
                    "pm_atmospheric": {
                        "description": "Particulate Matter concentration μg/m3 (atmospheric environment)",
                        "pm10_0": "PM 10",
                        "pm1_0": "PM 1.0",
                        "pm2_5": "PM 2.5"
                    },
                    "pm_factory": {
                        "description": "Particulate Matter concentration μg/m3 (factory environment)",
                        "pm10_0": "PM 10",
                        "pm1_0": "PM 1.0",
                        "pm2_5": "PM 2.5"
                    },
                    "rain": "Total Rainfall, mm",
                    "temp": {
                        "average": "Average temperature within the hour interval",
                        "max": "Maximum temperature within the hour interval",
                        "min": "Minimum temperature within the hour interval"
                    },
                    "timestamp": "Timestamp",
                    "weather": {
                        "description": "Descriptive weather condition",
                        "main_condition": "Vague weather condition"
                    },
                    "wind_spd": "Wind speed, m/s"
                }
            ]
        )

    st.markdown("<div class='section-title'>/data/pm</div>", unsafe_allow_html=True)
    st.markdown("<div class='parameter-text'>Get the PM data</div>", unsafe_allow_html=True)
    st.code("/data/pm?start_date={start_date}&end_date={end_date}&skip={skip}&limit={limit}", language="python")
    parameter_data()
    with st.expander("/data/pm"):
        st.json(
            [
                {
                    "pm_atmospheric": {
                        "description": "Particulate Matter concentration μg/m3 (atmospheric environment)",
                        "pm10_0": "PM 10",
                        "pm1_0": "PM 1.0",
                        "pm2_5": "PM 2.5"
                    },
                    "pm_factory": {
                        "description": "Particulate Matter concentration μg/m3 (factory environment)",
                        "pm10_0": "PM 10",
                        "pm1_0": "PM 1.0",
                        "pm2_5": "PM 2.5"
                    },
                    "timestamp": "Timestamp"
                }
            ]
        )

    st.markdown("<div class='section-title'>/data/aqi</div>", unsafe_allow_html=True)
    st.markdown("<div class='parameter-text'>Get the AQI data</div>", unsafe_allow_html=True)
    st.code("/data/aqi?start_date={start_date}&end_date={end_date}&skip={skip}&limit={limit}", language="python")
    parameter_data()
    with st.expander("/data/aqi"):
        st.json(
            [
                {
                    "aqi": "Air Quality Index",
                    "timestamp": "Timestamp"
                }
            ]
        )

    st.markdown("<div class='section-title'>/data/particle</div>", unsafe_allow_html=True)
    st.markdown("<div class='parameter-text'>Get the particle data</div>", unsafe_allow_html=True)
    st.code("/data/particle?start_date={start_date}&end_date={end_date}&skip={skip}&limit={limit}", language="python")
    parameter_data()
    with st.expander("/data/particle"):
        st.json(
            [
                {
                    "particles_count": {
                        "description": "Particle count in 0.1 liter or air",
                        "pcnt_0_3": "Diameter beyond 0.3 um",
                        "pcnt_0_5": "Diameter beyond 0.5 um",
                        "pcnt_10_0": "Diameter beyond 10 um",
                        "pcnt_1_0": "Diameter beyond 1 um",
                        "pcnt_2_5": "Diameter beyond 2.5 um",
                        "pcnt_5_0": "Diameter beyond 5 um"
                    },
                    "timestamp": "Timestamp"
                }
            ]
        )

    st.markdown("<div class='section-title'>/data/summary</div>", unsafe_allow_html=True)
    st.markdown("<div class='parameter-text'>Get the aggregated data in the specified date and period (min, max, average)</div>", unsafe_allow_html=True)
    st.code("/data/summary?period={period}&date={date}", language="python")
    parameter_head()
    with st.container(border=True):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.write("period")
        with col2:
            st.write("'weekly' or 'daily'")
        with col3:
            st.write('daily')
        with col4:
            st.write("Determine the time period of the data returned")
    with st.container(border=True):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.write("date")
        with col2:
            st.write("YYYY-MM-DD")
        with col3:
            st.write("Today's date")
        with col4:
            st.write("Determine the start date of the data returned (inclusive)")
    with st.expander("/data/summary"):
        st.json(
            [
                {
                    "start_time": {
                        "timestamp": "Timestamp"
                    },
                    "end_time": {
                        "timestamp": "Timestamp"
                    },
                    "average": "The average value of each attributes in the specific interval (except 'rain' which is the summation)",
                    "max": "The maximum value of each attributes in the specific interval",
                    "min": "The minimum value of each attributes in the specific interval"
                }
            ]
        )

    st.markdown("<div class='section-title'>/data/summary/custom</div>", unsafe_allow_html=True)
    st.markdown("<div class='parameter-text'>Get the aggregated data in the specific interval (min, max, average)</div>", unsafe_allow_html=True)
    st.code("/data/summary/custom?start_date={start_date}&end_date={end_date}", language="python")
    parameter_head()
    with st.container(border=True):
        col1, col2, col3, col4 = st.columns(4)
        with st.container(border=True):
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.write("start_date")
            with col2:
                st.write("YYYY-MM-DD")
            with col3:
                st.write("The oldest date of the data")
            with col4:
                st.write("Determine the start date of the data returned (inclusive)")

        with st.container(border=True):
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.write("end_date")
            with col2:
                st.write("YYYY-MM-DD")
            with col3:
                st.write("Today's date")
            with col4:
                st.write("Determine the end date of the data returned (exclusive)")
    with st.expander("/data/summary/custom"):
        st.json(
            [
                {
                    "start_time": {
                        "timestamp": "Timestamp"
                    },
                    "end_time": {
                        "timestamp": "Timestamp"
                    },
                    "average": "The average value of each attributes in the specific interval (except 'rain' which is the summation)",
                    "max": "The maximum value of each attributes in the specific interval",
                    "min": "The minimum value of each attributes in the specific interval"
                }
            ]
        )

with forcast_tab:

    st.markdown("<div class='section-title'>/forecast/1day</div>", unsafe_allow_html=True)
    st.markdown("<div class='parameter-text'>Get the next 24 hour forecast</div>", unsafe_allow_html=True)
    st.code("/forecast/1day?limit={limit}", language="python")
    parameter_forecast()
    with st.expander("/forecast/1day"):
        st.json(
            [
                {
                    "aqi": "AQI at the corresponding timestamp",
                    "pm10_0": "PM 10 concentration at the corresponding timestamp",
                    "pm2_5": "PM 2.5 concentration at the corresponding timestamp",
                    "timestamp": "Timestamp"
                }
            ]
        )

    st.markdown("<div class='section-title'>/forecast/3day</div>", unsafe_allow_html=True)
    st.markdown("<div class='parameter-text'>Get the next 72 hour forecast</div>", unsafe_allow_html=True)
    st.code("/forecast/3day?limit={limit}", language="python")
    parameter_forecast()
    with st.expander("/forecast/3day"):
        st.json(
            [
                {
                    "aqi": "AQI at the corresponding timestamp",
                    "pm10_0": "PM 10 concentration at the corresponding timestamp",
                    "pm2_5": "PM 2.5 concentration at the corresponding timestamp",
                    "timestamp": "Timestamp"
                }
            ]
        )

with raw_tab:
    st.markdown("<div class='section-title'>/raw/primary</div>", unsafe_allow_html=True)
    st.markdown("<div class='parameter-text'>Get the primary data</div>", unsafe_allow_html=True)
    st.code("/raw/primary?limit={limit}&sort={sort}", language="python")
    parameter_raw()

    st.markdown("<div class='section-title'>/raw/secondary</div>", unsafe_allow_html=True)
    st.markdown("<div class='parameter-text'>Get the secondary data</div>", unsafe_allow_html=True)
    st.code("/raw/secondary?limit={limit}&sort={sort}", language="python")
    parameter_raw()

    st.markdown("<div class='section-title'>/raw/hourly</div>", unsafe_allow_html=True)
    st.markdown("<div class='parameter-text'>Get the hourly data</div>", unsafe_allow_html=True)
    st.code("/raw/hourly?limit={limit}&sort={sort}", language="python")
    parameter_raw()
