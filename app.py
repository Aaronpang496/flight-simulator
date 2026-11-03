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

path = Path(__file__).resolve().with_name("game.html")

try:
    html = path.read_text(encoding="utf-8")
except (OSError, UnicodeError) as error:
    st.error(
        "Could not open game.html. It must be beside app.py. "
        f"Details: {error}"
    )
    st.stop()

components.html(html, height=1150, scrolling=True)
