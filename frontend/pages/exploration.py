"""Interactive visualisation dashboard for data exploration."""
from datetime import datetime
import time
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

    details summary {{
        font-size: 1.2em;
        font-weight: bold;
        background-color: {head_text};
        color: {color_4};
        padding: 10px;
        border-radius: 10px;
        cursor: pointer;
    }}
    
    details summary:hover {{
        background-color: {color_3};
        color: {head_text};
    }}
    
    details[open] summary {{
        background-color: {color_4};
        color: {head_text};
    }}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>Explore our Data!</div>", unsafe_allow_html=True)

attr_list = [
        'Timestamp',
        'PM 1.0',
        'PM 2.5',
        'PM 10',
        'AQI',
        'Particles > 0.3 μm',
        'Particles > 0.5 μm',
        'Particles > 1.0 μm',
        'Particles > 2.5 μm',
        'Particles > 5.0 μm',
        'Particles > 10.0 μm',
        'Temperature',
        'Humidity',
        'Wind Speed',
        'Light',
        'Cloud',
        'Rainfall'
]

with st.container(border=True):
    peak_help = """
# Peaked & Bottomed Statistics

- **Select attribute**

### Display
- **Peaked**
  - Peaked date and value of the attribute
  - The dataset of the peak day

- **Bottomed**
  - Bottomed date and value of the attribute
  - The dataset of the bottom day
"""
    st.markdown(
        "<div class='section-title'>📑 Peaked & Bottomed Statistics</div>",
        unsafe_allow_html=True,
        help=peak_help
    )

    selected_attr = st.selectbox(
        "Select Attribute",
        attr_list,
        index=2,
        key='exploration_peak_selected_attr'
    )

    with st.spinner('Loading Data...'):
        time.sleep(1)
        peaked_data, peaked_val, peaked_time, bottomed_data, bottomed_val, bottomed_time = graph.stats.find_peaked_and_bottomed(selected_attr)

        col1, col2 = st.columns(2)
        with col1:
            with st.container(border=True):
                st.header(f"📈 Most recent Peaked - {selected_attr}")
                st.subheader(peaked_time)
                st.markdown(f"<div class='main-title'>{peaked_val:2f}</div>", unsafe_allow_html=True)

                with st.expander("Dataset"):
                    st.dataframe(peaked_data)
        with col2:
            with st.container(border=True):
                st.header(f"📉 Most recent Bottomed - {selected_attr}")
                st.subheader(bottomed_time)
                st.markdown(f"<div class='main-title'>{bottomed_val:2f}</div>", unsafe_allow_html=True)

                with st.expander("Dataset"):
                    st.dataframe(bottomed_data)


with st.container(border=True):
    scatter_help = """
# Scatter Plot

- **Select categorical hue**
- **Select Datetime Range**
- **Select exactly 2 attributes**

### Display

- Scatter plot of the 2 attributes with the selected hue, using data from the specified datetime range.
"""
    st.markdown(
        "<div class='section-title'>⭐ Scatter Plot</div>",
        unsafe_allow_html=True,
        help=scatter_help
    )

    # Hue options
    hue_options = ['None', 'Weather', 'Weather (Detailed)', 'Day of Week']
    hue_selected = st.segmented_control(
        "Select Hue",
        hue_options,
        selection_mode="single",
        default='None',
        key="exploration_scatter_hue"
    )

    # Date range filter
    col1, col2 = st.columns(2)
    start_date = col1.date_input('Start Datetime', format="DD/MM/YYYY", key="exploration_scatter_start_date")
    end_date = col2.date_input('End Datetime', format="DD/MM/YYYY", key="exploration_scatter_end_date")

    col1, col2 = st.columns(2)
    start_time = col1.time_input('input time',
                                 label_visibility="collapsed",
                                 key="exploration_scatter_start_time",
                                 value="00:00",
                                 step=3600)
    end_time = col2.time_input('input time',
                               label_visibility="collapsed",
                               key="exploration_scatter_end_time",
                               value="23:00",
                               step=3600)

    start_datetime = datetime.combine(start_date, start_time)
    end_datetime = datetime.combine(end_date, end_time)

    valid_daterange = end_datetime > start_datetime
    if not valid_daterange:
        st.warning("Start Datetime must be before End Datetime.")

    # Attributes selection
    selected_attr = st.multiselect(
        "Select exactly 2 Attributes",
        attr_list,
        ["Timestamp", "PM 2.5"],
        key="exploration_scatter_selected_attrs"
    )
    valid_attr = len(selected_attr) == 2
    if not valid_attr:
        st.warning('Please select exactly two options.')

    valid = valid_daterange and valid_attr
    if valid:
        with st.spinner("Generating..."):
            time.sleep(2)
            st.plotly_chart(
                graph.scatter_plot.generate_scatter_plot(
                    sel_attr=selected_attr,
                    sel_hue=hue_selected,
                    start_datetime=start_datetime,
                    end_datetime=end_datetime
                )
            )


with st.container(border=True):
    bar_help = """
# Bar Chart

- **Select categorical hue**
- **Select bar mode** (how to display a bar chart)
- **Select Datetime Range**
- **Select attribute**

### Display

- Bar chart with the specified mode of the attribute statistics, including `mean`, `median`, `mode`, `min`, and `max` with the selected hue, using data from the specified datetime range.
"""
    st.markdown(
        "<div class='section-title'>📶 Bar Chart</div>",
        unsafe_allow_html=True,
        help=bar_help
    )

    # Hue options
    hue_options = ['None', 'Weather', 'Weather (Detailed)', 'Day of Week']
    hue_selected = st.segmented_control(
        "Select Hue",
        hue_options,
        selection_mode="single",
        default='None',
        key="exploration_bar_hue"
    )

    # Bar mode
    bar_mode_options = ["group", "stack", "overlay", "relative"]
    bar_mode_descriptions = [
        "Bars are placed side-by-side (grouped)",
        "Bars are stacked on top of each other",
        "Bars are drawn on top of each other with transparency",
        "Bars are stacked relative to zero, separating positive and negative values"
    ]
    bar_mode = st.radio(
        "Select Bar Mode",
        bar_mode_options,
        captions=bar_mode_descriptions,
        key="exploration_bar_mode",
        horizontal=False
    )

    # Date range filter
    col1, col2 = st.columns(2)
    start_date = col1.date_input('Start Datetime', format="DD/MM/YYYY", key="exploration_bar_start_date")
    end_date = col2.date_input('End Datetime', format="DD/MM/YYYY", key="exploration_bar_end_date")

    col1, col2 = st.columns(2)
    start_time = col1.time_input('input time',
                                 label_visibility="collapsed",
                                 key="exploration_bar_start_time",
                                 value="00:00",
                                 step=3600)
    end_time = col2.time_input('input time',
                               label_visibility="collapsed",
                               key="exploration_bar_end_time",
                               value="12:00",
                               step=3600)

    start_datetime = datetime.combine(start_date, start_time)
    end_datetime = datetime.combine(end_date, end_time)

    valid_daterange = end_datetime > start_datetime
    if not valid_daterange:
        st.warning("Start Datetime must be before End Datetime.")

    # Attributes selection
    selected_attr = st.selectbox(
        "Select Attribute",
        attr_list,
        index=2,
        key='exploration_bar_selected_attr'
    )

    valid = valid_daterange
    if valid:
        with st.spinner("Generating..."):
            time.sleep(2)
            st.plotly_chart(
                graph.bar_chart.generate_bar_chart(
                    sel_attr=selected_attr,
                    sel_hue=hue_selected,
                    barmode=bar_mode,
                    start_datetime=start_datetime,
                    end_datetime=end_datetime
                )
            )

with st.container(border=True):
    hist_help = """
# Histogram

- **Select categorical hue**
- **Select Datetime Range**
- **Select attribute**

### Display

- Histogram (Density mode) of the attribute with the selected hue, using data from the specified datetime range.
"""
    st.markdown(
        "<div class='section-title'>📊 Histogram</div>",
        unsafe_allow_html=True,
        help=hist_help
    )

    # Hue options
    hue_options = ['None', 'Weather', 'Weather (Detailed)', 'Day of Week']
    hue_selected = st.segmented_control(
        "Select Hue",
        hue_options,
        selection_mode="single",
        default='None',
        key="exploration_hist_hue"
    )

    # Date range filter
    col1, col2 = st.columns(2)
    start_date = col1.date_input('Start Datetime', format="DD/MM/YYYY", key="exploration_hist_start_date")
    end_date = col2.date_input('End Datetime', format="DD/MM/YYYY", key="exploration_hist_end_date")

    col1, col2 = st.columns(2)
    start_time = col1.time_input('input time',
                                 label_visibility="collapsed",
                                 key="exploration_hist_start_time",
                                 value="00:00",
                                 step=3600)
    end_time = col2.time_input('input time',
                               label_visibility="collapsed",
                               key="exploration_hist_end_time",
                               value="12:00",
                               step=3600)

    start_datetime = datetime.combine(start_date, start_time)
    end_datetime = datetime.combine(end_date, end_time)

    valid_daterange = end_datetime > start_datetime
    if not valid_daterange:
        st.warning("Start Datetime must be before End Datetime.")

    # Attributes selection
    selected_attr = st.selectbox(
        "Select Attribute",
        attr_list,
        index=2,
        key='exploration_hist_selected_attr'
    )

    valid = valid_daterange
    if valid:
        with st.spinner("Generating..."):
            time.sleep(2)
            st.plotly_chart(
                graph.histogram.generate_histogram(
                    sel_attr=selected_attr,
                    sel_hue=hue_selected,
                    start_datetime=start_datetime,
                    end_datetime=end_datetime
                )
            )

st.markdown("<div class='section-title'>❓ Explore more!</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    with st.expander("PM 2.5: Rain vs No Rain"):
        st.plotly_chart(graph.bar_chart.pm2_5_rain)
with col2:
    with st.expander("Week"):
        st.plotly_chart(graph.box_plot.pm10_0_day_of_week)
        st.plotly_chart(graph.histogram.day_of_week)
with col3:
    with st.expander("Correlation"):
        st.plotly_chart(graph.heatmap.corr)

col1, col2 = st.columns(2)
with col1:
    with st.expander("Weather Condition: Main"):
        st.plotly_chart(graph.box_plot.pm10_0_weather_main)
        st.plotly_chart(graph.histogram.weather_main)
with col2:
    with st.expander("Weather Condition: Detailed"):
        st.plotly_chart(graph.box_plot.pm10_0_weather_con)
        st.plotly_chart(graph.histogram.weather_con)
