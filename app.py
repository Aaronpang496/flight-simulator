from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Island Flight",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    .block-container {
        padding: 0.5rem;
        max-width: 1500px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

game_file = Path(__file__).with_name("game.html")

if game_file.is_file():
    components.html(
        game_file.read_text(encoding="utf-8"),
        height=1500,
        scrolling=True,
    )
else:
    st.error("game.html is missing. Put it in the same folder as app.py.")
