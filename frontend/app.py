"""Main frontend application."""
import streamlit as st
from streamlit_extras.let_it_rain import rain

st.set_page_config(
    page_title="Raindrop Dust",
    layout="wide",
)

st.markdown(f"""
<style>
    .main-title {{
        font-size: 5em;
    }}
</style>
""", unsafe_allow_html=True)

rain(
    emoji="💧",
    font_size=12,
    falling_speed=4,
    animation_length="infinite",
)

st.markdown(f"""
<div style="
    font-size: 5em;
    font-weight: bold;
    color: #94B4C1;
    text-align: center;
    margin-bottom: 1rem;">
    Raindrop <span style='color:white;'>Dust</span> 🌫️
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
with col1:
    st.page_link("pages/current.py", label="Current", icon="🆕")
with col2:
    st.page_link("pages/exploration.py", label="Exploration", icon="🔍")
with col3:
    st.page_link("pages/descriptive.py", label="Descriptive", icon="📈")
with col4:
    st.page_link("pages/predictive.py", label="Predictive", icon="🔮")
with col5:
    st.page_link("pages/dataset.py", label="Dataset", icon="🗂️")
with col6:
    st.page_link("pages/api.py", label="API", icon="🗝️")
with col7:
        st.page_link("pages/api_docs.py", label="Documents", icon="📄")

st.markdown("<p style='text-align: center; font-size: 24px; color: #94B4C1'>━━━━━·. ݁₊ ⊹ . ݁˖ .݁・:・:. ݁₊⊹ . ݁  ݁・:・. ݁₊ ⊹. ݁˖ :・:·━━━━━ ️</p>", unsafe_allow_html=True)

current_page = st.Page("pages/current.py", title="Current", icon="🆕")
exploration_page = st.Page("pages/exploration.py", title="Exploration", icon="🔍")
descriptive_page = st.Page("pages/descriptive.py", title="Descriptive", icon="📈")
predictive_page = st.Page("pages/predictive.py", title="Predictive", icon="🔮")
dataset_page = st.Page("pages/dataset.py", title="Dataset", icon="🗂️")
api_page = st.Page("pages/api.py", title="API", icon="🗝️")
api_docs_page = st.Page("pages/api_docs.py", title="Documents", icon="📄")

pg = st.navigation({
    "Visualisation": [current_page, exploration_page, descriptive_page, predictive_page],
    "Data": [dataset_page],
    "API": [api_page, api_docs_page],
})

pg.run()
