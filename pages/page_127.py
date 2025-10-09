import streamlit as st
from inventory import display_inventory, check_inventory
from utils import stream_text, set_cookies, called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    is_good = called_cookies()
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=127)

fr_text = """
Après avoir marché pendant une heure, les Drakkarims
s'arrêtent soudain tandis qu'une énorme créature couverte
d'écaillés grises s'approche sur le chemin. Lorsque la bête
répugnante se trouve tout près de vous, son haleine fétide vous
fait grimacer. Le monstre pousse un rugissement et vous saisit la
tête entre ses pattes palmées. Vous entendez alors un
craquement: votre colonne vertébrale vient de se briser à hauteur
de votre cou. C'est d'ailleurs le dernier son qui vous parvient en
ce bas monde, car vous mourez à l'instant même.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Votre mission s'achève ici."""
        )
    )
    ls_death()
    
    st.session_state.last_page_number = st.session_state.current_page_number

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")