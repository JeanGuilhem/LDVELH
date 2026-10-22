import streamlit as st
from inventory import (
    display_inventory,
    check_inventory,
    end_page,
    choose_item_to_lose,
    change_endurance,
    is_new_page, show_illustrations)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=144)

fr_text = """
Vous vous frayez un chemin à coups de coude dans la foule qui se
presse sur la grand-rue. Vous apercevez un peu plus loin la
silhouette massive de la citadelle qui abrite le Palais du Roi. Les
habitants de Holmgard, saisis de panique, courent en tous sens,
tandis que retentissent les cris des Kraans qui tournoient dans le
ciel de la ville. Dans la bousculade, quelqu'un vous vole l'un des
objets contenus dans votre Sac à Dos. Si vous n'avez plus de Sac à
Dos, c'est une arme qu'on vous dérobe. Rayez l'objet ou l'arme
perdue de votre Feuille d'Aventure (c'est vous qui choisissez ce
qu'on vous a volé). Un cheval emballé, qui tire une charrette,
passe devant vous à toute allure et vous heurte en vous projetant
contre une porte cochère. Vous êtes à moitié assommé et vous
perdez 2 points D'ENDURANCE. Vous vous relevez en titubant,
mais, au même moment, la porte s'ouvre à la volée et un vieil
homme décrépit se précipite sur vous en brandissant un couteau
à viande. Il est fou à lier et il vous faut le combattre ou tenter de
fuir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    # un objet du Sac à Dos est volé, ou une arme si le Sac à Dos est absent ou vide
    candidats = st.session_state.backpack if st.session_state.backpack else st.session_state.weapons
    if choose_item_to_lose(list(candidats), key="theft", label="Choisissez ce qu'on vous a volé :"):
        st.write_stream(stream_text("Si vous choisissez de le combattre, rendez-vous au :"))
        st.page_link("tomes/tome1/page_63.py", label="63", icon="📄")

        st.write_stream(stream_text("Si vous préférez essayer d'éviter l'affrontement, rendez-vous au :"))
        st.page_link("tomes/tome1/page_217.py", label="217", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
