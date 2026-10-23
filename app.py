from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Island Flight",
    page_icon="✈️",
    layout="centered",
)

st.title("✈️ Island Flight")
st.caption(
    "Updated takeoff physics • Touch flight controls • "
    "Selectable airport settings"
)

html = Path(__file__).with_name("game.html").read_text(
    encoding="utf-8"
)

components.html(html, height=1050, scrolling=True)
