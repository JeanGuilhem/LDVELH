import streamlit as st
from utils import stream_text
from text import fr_presentation

st.set_page_config(
    page_title="Accueil",
    page_icon="🏠",
    menu_items={
        "Report a bug": "https://github.com/JeanGuilhem/Vous-tes-le-H-ros/issues",
    },
    initial_sidebar_state="collapsed",
)
st.title("Bienvenue ! ")
st.divider()

if "intro" not in st.session_state:
    st.write_stream(stream_text(text=fr_presentation))
    
st.session_state.intro = True
st.page_link("pages/crafting_hero.py", label="Démarrer mon aventure", icon="⚔️")
st.page_link("pages/rules.py", label="Règles", icon="🧙‍♂️")
