import streamlit as st
from frontend.components import graph


# Tap: Today
# latest data
# day summary
# line

# Tap: This week
# week summary
# line

st.title("Current Condition")

# Create tabs for Today and This Week
today_tab, week_tab = st.tabs(["Today", "This Week"])

with today_tab:
    st.header("Today's Air Quality")
    # Display latest data summary (you can add your summary here)
    st.dataframe(graph.stats.today)
    # Example placeholder for summary, replace with your actual summary code
    st.write("Summary of today's air quality data goes here.")

    # Plot today's AQI time series line graph
    st.plotly_chart(graph.line_graph.aqi_ts_today, use_container_width=True)

with week_tab:
    st.header("This Week's Air Quality")
    # Display weekly summary (add your summary here)
    st.markdown("### Weekly Summary")
    st.write("Summary of this week's air quality data goes here.")

    # Plot this week's AQI time series line graph
    st.plotly_chart(graph.line_graph.aqi_ts_week, use_container_width=True)
