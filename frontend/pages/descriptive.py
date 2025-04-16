import streamlit as st
import plotly.express as px

from frontend.utils.dataframe import df


# Visualise
fig = px.line(df, x='ts', y= 'aqi', title='AQI Line Chart')
st.plotly_chart(fig)
