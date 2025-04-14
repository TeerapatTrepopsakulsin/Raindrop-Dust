import streamlit as st

st.title('Raindrop Dust')
descriptive_page = st.Page("pages/descriptive.py", title="Descriptive", url_path="/descriptive", icon="😇")
predictive_page = st.Page("pages/predictive.py", title="Predictive", icon="😭")
dataset_page = st.Page("pages/dataset.py", title="Dataset", icon="🤣")
api_page = st.Page("pages/api.py", title="API", icon="😍")

pg = st.navigation({
    "Visualisation": [descriptive_page, predictive_page],
    "Data": [dataset_page],
    "API": [api_page]
})

pg.run()
