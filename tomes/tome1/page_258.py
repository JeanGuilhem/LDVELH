import streamlit as st
from inventory import display_inventory, check_inventory, end_page, is_new_page, lose_backpack, lose_all_weapons, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=258)

fr_text = """
Grâce à votre Maîtrise Psychique de la Matière, vous parvenez en
quelques instants à dénouer vos liens. Vous attendez alors le
moment propice pour vous enfuir et, soudain, vous vous mettez à
courir à toutes jambes en direction des sous-bois touffus. Des
flèches noires sifflent à vos oreilles mais, bientôt, vous vous êtes
enfoncé suffisamment loin dans l'épaisse végétation pour être sûr
d'avoir échappé à vos poursuivants. Vous avez perdu votre Sac à
Dos et vos Armes, mais vous êtes indemne. Il ne vous reste plus à
présent qu'à poursuivre votre chemin parmi les arbres de la
forêt.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        lose_backpack()
        lose_all_weapons()

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome1/page_50.py", label="50", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
