import streamlit as st


st.title('Raindrop Dust')
current_page = st.Page("pages/current.py", title="Current", icon="😶‍🌫️")
exploration_page = st.Page("pages/exploration.py", title="Exploration", icon="🤯")
descriptive_page = st.Page("pages/descriptive.py", title="Descriptive", icon="🤤")
predictive_page = st.Page("pages/predictive.py", title="Predictive", icon="🥹")
dataset_page = st.Page("pages/dataset.py", title="Dataset", icon="😎")
api_page = st.Page("pages/api.py", title="API", icon="😍")
api_docs_page = st.Page("pages/api_docs.py", title="Documents", icon="😷")

pg = st.navigation({
    "Visualisation": [current_page, exploration_page, descriptive_page, predictive_page],
    "Data": [dataset_page],
    "API": [api_page, api_docs_page],
})

pg.run()
