from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Island Flight", page_icon="✈️", layout="wide")

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

game_file = Path(__file__).resolve().with_name("game.html")

try:
    html = game_file.read_text(encoding="utf-8")
except FileNotFoundError:
    st.error("game.html was not found. Place it beside app.py and check the filename.")
    st.stop()
except (OSError, UnicodeError):
    st.error("game.html could not be read as a UTF-8 text file.")
    st.stop()

components.html(html, height=1050, scrolling=True)
