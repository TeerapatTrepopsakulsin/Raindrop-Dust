import streamlit as st
from frontend.components import graph


# Visualise
fig = graph.line_graph.aqi_ts_today
st.plotly_chart(fig)
