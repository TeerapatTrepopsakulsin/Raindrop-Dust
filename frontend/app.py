import streamlit as st

st.title('Raindrop Dust')
descriptive_page = st.Page("pages/descriptive.py", title="Descriptive", icon="😇")
predictive_page = st.Page("pages/predictive.py", title="Predictive", icon="😭")
dataset_page = st.Page("pages/dataset.py", title="Dataset", icon="🤣")

pg = st.navigation({
    "Visualisation": [descriptive_page, predictive_page],
    "Data": [dataset_page],
})

pg.run()
