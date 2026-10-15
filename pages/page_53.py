import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai
from utils import stream_text, set_cookies, called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=53)

fr_text = """
Une douleur fulgurante vous déchire soudain la jambe droite :
vous venez de vous tordre la cheville et vous trébuchez en
tombant tête la première. Entraîné par le poids de votre corps,
vous roulez alors sur vous-même le long du flanc de la colline
avant d'atterrir enfin dans un fossé où vous perdez connaissance.
Vous êtes réveillé par une autre douleur: quelque chose s'enfonce
dans votre poitrine. C'est le fer de la lance d'un Glok. La créature
vous plaque au sol en vous gratifiant d'un sourire diabolique, et,
d'un geste instinctif, vous essayez de saisir votre arme, mais elle
a disparu. Vous êtes désormais sans défense contre les Gloks
cruels et avant que toute lumière s'éteigne, vous apercevez dans
une ultime vision l'extrémité de la lance qui s'abat à présent sur
votre gorge. Votre mission vient de prendre fin.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    ls_death()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
