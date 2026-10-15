import streamlit as st
from inventory import (
    display_inventory,
    check_inventory,
    end_page,
    is_new_page,
    lose_all_weapons,
    lose_backpack,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=181)

fr_text = """
Instinctivement, vous plongez en avant pour éviter le carreau de
l'arbalète. Le brigand tire et vous sentez la manche de votre
tunique se déchirer tandis que le projectile vous écorche le bras
gauche. Vous remerciez les Dieux de vous avoir protégé et vous
prenez vos jambes à votre cou. Les autres bandits n'ont pas
d'arbalètes ni d'arcs et ils ont tôt fait d'abandonner la poursuite.
Quelques instants plus tard, ils sont loin derrière vous et vous
êtes sauf. Vous avez perdu votre Équipement, mais pas la vie.
Vous faites une brève halte pour panser l'écorchure causée par le
carreau d'arbalète puis vous vous remettez en route en direction
de la capitale.
"""

# l'Équipement (armes et Sac à Dos) est perdu ; l'or et les Objets Spéciaux sont conservés
if is_new_page():
    lose_backpack()
    lose_all_weapons()

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("pages/page_288.py", label="288", icon="📄")

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
