import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, called_cookies, handle_repas
from text import fr_unkown_kai

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=37)

fr_text = """
Vous vous sentez fatigué et affamé, et il vous faut faire une halte
pour prendre un Repas. Après avoir mangé, vous rebroussez
chemin jusqu'à la citadelle et vous marchez le long de ses hautes
murailles de pierre. Vous découvrez une autre entrée dans le mur
est, gardée, elle aussi, par deux soldats en armes.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    handle_repas()

    st.write_stream(
        stream_text("Si vous voulez vous approcher d'eux et leur raconter votre histoire, rendez-vous au :")
    )
    st.page_link("tomes/tome1/page_289.py", label="289", icon="📄")

    st.write_stream(
        stream_text("Si vous maîtrisez la Discipline Kaï du Camouflage, rendez-vous au :")
    )
    if has_kai("Le Camouflage"):
        st.page_link("tomes/tome1/page_282.py", label="282", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome1/page_282.py", label="282", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
