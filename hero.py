import streamlit as st
from save import apply_save, page_path, read_save
from inventory import init_state
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
else:
    st.write(fr_presentation)

saved_game = read_save()
if isinstance(saved_game, dict):
    if st.button(
        f"Reprendre mon aventure (paragraphe {saved_game['current_page_number']})", icon="📜"
    ):
        init_state()
        apply_save(saved_game)
        st.session_state.game_phase = "playing"
        st.switch_page(page_path(saved_game["current_page_number"]))
    st.caption("Démarrer une nouvelle aventure effacera votre sauvegarde.")

st.page_link("pages/crafting_hero.py", label="Démarrer une nouvelle aventure", icon="⚔️")
st.page_link("pages/rules.py", label="Règles", icon="🧙‍♂️")
