
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
                current_page_number=327)

fr_text = """
Quelques minutes plus tard, vous voyez les Kraans apparaître au-
dessus d'une petite colline située derrière vous. Vous en
dénombrez au moins seize qui sont chacun montés par deux
Gloks. Ces derniers sont armés de lances et coiffés de casques de
bronze. Vous les entendez aussitôt pousser des grognements
satisfaits : ils vous ont repéré... Vous bondissez alors en direction
de l'entrée du tunnel quelque huit mètres plus bas, mais votre
botte se prend dans un buisson et vous tombez de tout votre
long. Dans votre chute, vous avez lâché votre Arme et vous êtes
désormais à la merci de vos adversaires. Fort heureusement,
votre fin est rapide: le premier Glok qui s'approche de vous
enfonce sa lance dans votre poitrine et vous transperce le cœur.
Vous mourez sur le coup. Votre mission s'achève ici, en même
temps que votre vie.
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
