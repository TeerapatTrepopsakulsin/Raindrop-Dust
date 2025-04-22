import streamlit as st

color_2 = "#94B4C1"

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
            st.write("limit")
        with col2:
            st.write("Integer")
        with col3:
            st.write(0)
        with col4:
            st.write("Determine the order of the data returned")

st.markdown("<div class='main-title'>API Documentation</div>", unsafe_allow_html=True)

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

    st.markdown("<div class='section-title'>/data</div>", unsafe_allow_html=True)
    st.markdown("<div class='parameter-text'>Get the data</div>", unsafe_allow_html=True)
    st.code("/data?start_date={start_date}&end_date={end_date}&skip={skip}&limit={limit}", language="python")
    parameter_data()

    st.markdown("<div class='section-title'>/data/pm</div>", unsafe_allow_html=True)
    st.markdown("<div class='parameter-text'>Get the PM data</div>", unsafe_allow_html=True)
    st.code("/data/pm?start_date={start_date}&end_date={end_date}&skip={skip}&limit={limit}", language="python")
    parameter_data()

    st.markdown("<div class='section-title'>/data/aqi</div>", unsafe_allow_html=True)
    st.markdown("<div class='parameter-text'>Get the AQI data</div>", unsafe_allow_html=True)
    st.code("/data/aqi?start_date={start_date}&end_date={end_date}&skip={skip}&limit={limit}", language="python")
    parameter_data()

    st.markdown("<div class='section-title'>/data/particle</div>", unsafe_allow_html=True)
    st.markdown("<div class='parameter-text'>Get the particle data</div>", unsafe_allow_html=True)
    st.code("/data/particle?start_date={start_date}&end_date={end_date}&skip={skip}&limit={limit}", language="python")
    parameter_data()

    st.markdown("<div class='section-title'>/data/summary</div>", unsafe_allow_html=True)
    st.markdown("<div class='parameter-text'>Get the summary data</div>", unsafe_allow_html=True)
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

    st.markdown("<div class='section-title'>/data/summary/custom</div>", unsafe_allow_html=True)
    st.markdown("<div class='parameter-text'>Get the summary data</div>", unsafe_allow_html=True)
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

with forcast_tab:

    st.markdown("<div class='section-title'>/forecast/1day</div>", unsafe_allow_html=True)
    st.markdown("<div class='parameter-text'>Get the next 24 hour forecast</div>", unsafe_allow_html=True)
    st.code("/forecast/1day?limit={limit}", language="python")
    parameter_forecast()

    st.markdown("<div class='section-title'>/forecast/3day</div>", unsafe_allow_html=True)
    st.markdown("<div class='parameter-text'>Get the next 72 hour forecast</div>", unsafe_allow_html=True)
    st.code("/forecast/3day?limit={limit}", language="python")
    parameter_forecast()

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
