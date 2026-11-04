from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="737 Island Hopper",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
        .block-container {
            padding-top: 0.4rem;
            padding-bottom: 0.5rem;
            padding-left: 0.4rem;
            padding-right: 0.4rem;
            max-width: 1600px;
        }

        header[data-testid="stHeader"] {
            display: none;
        }

        footer {
            display: none;
        }

        iframe {
            border: 0;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

game_path = Path(__file__).with_name("game.html")

if game_path.exists():
    components.html(
        game_path.read_text(encoding="utf-8"),
        height=1320,
        scrolling=True,
    )
else:
    st.error("game.html is missing. Put it beside app.py.")
