import streamlit as st
from frontend.utils.dataframe import pmr_df, snd_df, hour_df


st.header('Dataset & Tables')

with st.expander("Primary Table"):
    st.dataframe(pmr_df)

with st.expander("Secondary Table"):
    st.dataframe(snd_df)

with st.expander("Hourly Table"):
    st.dataframe(hour_df)
