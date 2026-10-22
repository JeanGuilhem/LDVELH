import streamlit as st
from inventory import display_inventory, check_inventory, end_page, is_new_page, lose_all_weapons, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=274)

fr_text = """
Dans votre hâte de fuir l'ennemi, vous vous prenez le pied dans la
racine d'un arbre et vous tombez tête la première en soulevant un
nuage de poussière et de feuilles. Vous vous relevez aussitôt et
vous courez vous réfugier dans la forêt, au pied de la colline. Au
bout de dix minutes de cette fuite éperdue, vous vous apercevez
que vous avez perdu vos Armes lors de votre chute. C'est fâcheux,
mais au moins, vous êtes vivant et vous avez toujours votre Sac à
Dos. Faisant contre mauvaise fortune bon cœur, vous poursuivez
votre chemin en vous enfonçant plus avant parmi les arbres.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        lose_all_weapons()

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome1/page_331.py", label="331", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
