from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Island Flight",
    page_icon="✈️",
    layout="wide",
)

st.markdown(
    """
    <style>
    .block-container {
        padding-top: 0.5rem;
        padding-bottom: 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

game_file = Path(__file__).resolve().with_name("game.html")

try:
    html = game_file.read_text(encoding="utf-8")
except (OSError, UnicodeError) as error:
    st.error(
        "Could not read game.html. Keep it beside app.py. "
        f"Details: {error}"
    )
    st.stop()

components.html(
    html,
    height=1250,
    scrolling=True,
)
