from datetime import datetime
import time
import streamlit as st
from frontend.components import graph


st.header("Explore our Data!")

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
    st.subheader('Peaked & Bottomed Statistics')

    selected_attr = st.selectbox(
        "Select Attribute",
        attr_list,
        index=2,
        key='exploration_peak_selected_attr'
    )

    with st.spinner('Loading Data...'):
        time.sleep(1)
        peaked_data, peaked_val, peaked_time, bottomed_data, bottomed_val, bottomed_time = graph.stats.find_peaked_and_bottomed(selected_attr)

        with st.container(border=True):
            st.header(f"📈 Most recent Peaked - {selected_attr}")
            st.subheader(peaked_time)
            st.title(f"{peaked_val:2f}")

            with st.expander("Dataset"):
                st.dataframe(peaked_data)

        with st.container(border=True):
            st.header(f"📉 Most recent Bottomed - {selected_attr}")
            st.subheader(bottomed_time)
            st.title(f"{bottomed_val:2f}")

            with st.expander("Dataset"):
                st.dataframe(bottomed_data)


with st.container(border=True):
    st.subheader('Scatter Plot')

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
    st.subheader('Bar Chart')

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
    st.subheader('Histogram')

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


with st.expander("Explore more!"):
    st.plotly_chart(graph.bar_chart.pm2_5_rain)
    st.plotly_chart(graph.box_plot.pm10_0_weather_main)
    st.plotly_chart(graph.box_plot.pm10_0_weather_con)
    st.plotly_chart(graph.box_plot.pm10_0_day_of_week)
    st.plotly_chart(graph.heatmap.corr)
    st.plotly_chart(graph.histogram.day_of_week)
    st.plotly_chart(graph.histogram.weather_con)
    st.plotly_chart(graph.histogram.weather_main)
