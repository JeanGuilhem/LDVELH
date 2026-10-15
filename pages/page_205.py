import streamlit as st
from inventory import display_inventory, check_inventory, end_page
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=205)

fr_text = """
Leur chef ramasse votre Équipement et vous fait signe d'avancer
le long du chemin. Les deux autres ont alors un sourire mauvais
et vous vous rendez soudain compte qu'il ne s'agit pas du tout de
soldats : ce sont des brigands déguisés. Vous prenez aussitôt la
fuite en courant à toutes jambes vers la capitale. Mais au même
instant, un frisson vous parcourt l'échiné : vous venez en effet
d'entendre derrière vous le déclic d'une arbalète que l'on arme.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    number = hazard_roll()
    if number is not None and number <= 4:
        st.page_link("pages/page_181.py", label="181", icon="📄")
    elif number is not None:
        st.page_link("pages/page_145.py", label="145", icon="📄")

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
