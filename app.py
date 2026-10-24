from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Island Flight",
    page_icon="✈️",
    layout="wide",
)

st.title("✈️ Island Flight")
st.caption(
    "3D cockpit prototype • Touch flight controls • "
    "Selectable airport settings • Simplified flight physics"
)

html = Path(__file__).with_name("game.html").read_text(
    encoding="utf-8"
)

components.html(
    html,
    height=1200,
    scrolling=True,
)
