from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

# 1. Setup the page
st.set_page_config(
    page_title="Island Flight",
    page_icon="✈️",
    layout="wide",
)

# 2. Clean up the padding so the game fills the screen
st.markdown(
    """
    <style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 3. Read your game.html file
html = Path(__file__).with_name("game.html").read_text(
    encoding="utf-8"
)

# 4. Render the game in an iframe
components.html(
    html,
    height=1050,
    scrolling=True,
)
