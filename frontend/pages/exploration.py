from datetime import datetime
import time
import streamlit as st
from frontend.components import graph
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
        background-color: #213448;
    }}
    
    details > summary::-webkit-details-marker {{
        display: none;
    }}
</style>
""", unsafe_allow_html=True)

custom_cmap = mcolors.LinearSegmentedColormap.from_list(
    "white_to_blue", [head_text, color_2]
)

def show_table(df, key_prefix=""):
    if st.toggle("❇️ Show full table (might be slow!)", value=False, key=f"{key_prefix}_toggle"):
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
    st.markdown("<div class='section-title'>📈 Peaked & 📉 Bottomed Statistics</div>", unsafe_allow_html=True)

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
            st.markdown(f"<div class='main-title'>{peaked_val:2f}</div>", unsafe_allow_html=True)

            with st.expander("Dataset"):
                show_table(peaked_data, key_prefix="peaked_data")

        with st.container(border=True):
            st.header(f"📉 Most recent Bottomed - {selected_attr}")
            st.subheader(bottomed_time)
            st.markdown(f"<div class='main-title'>{bottomed_val:2f}</div>", unsafe_allow_html=True)

            with st.expander("Dataset"):
                show_table(bottomed_data, key_prefix="bottomed_data")


with st.container(border=True):
    st.markdown("<div class='section-title'>🎆 Scatter Plot</div>", unsafe_allow_html=True)

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
    st.markdown("<div class='section-title'>📶 Bar Chart</div>", unsafe_allow_html=True)

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
    st.markdown("<div class='section-title'>📊 Histogram</div>", unsafe_allow_html=True)

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


st.markdown("<div class='section-title'>🔍 More</div>", unsafe_allow_html=True)
with st.expander("Explore more!"):
    st.plotly_chart(graph.bar_chart.pm2_5_rain)
    st.plotly_chart(graph.box_plot.pm10_0_weather_main)
    st.plotly_chart(graph.box_plot.pm10_0_weather_con)
    st.plotly_chart(graph.box_plot.pm10_0_day_of_week)
    st.plotly_chart(graph.heatmap.corr)
    st.plotly_chart(graph.histogram.day_of_week)
    st.plotly_chart(graph.histogram.weather_con)
    st.plotly_chart(graph.histogram.weather_main)
