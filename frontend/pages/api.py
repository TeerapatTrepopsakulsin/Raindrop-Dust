import streamlit as st
from frontend.utils.api import get_api_res

color_2 = "#94B4C1"

st.markdown(f"""
<style>
    .main-title {{
        font-size: 3em;
        font-weight: bold;
        color: {color_2};
        margin-bottom: 0.3em;
    }}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>🌐 API Endpoints</div>", unsafe_allow_html=True)

api = st.text_input(
    "Enter API Path",
    value="/data/latest?limit=1",
    key="api_path_input",
    help="See API docs page",
    placeholder="API Path e.g. /data/latest?limit=1")

try:
    response = get_api_res(api)
except Exception as e:
    st.error('🚫 Invalid API Path')
else:
    if response.status_code == 200:
        data = response.json()
        st.json(data, expanded=True)
    else:
        st.error('🚫 Invalid API Path')
