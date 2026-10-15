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
                current_page_number=54)

fr_text = """
Il semble que le ciel soit resté sourd à vos prières car un instant
plus tard, une lance siffle à vos oreilles et vient se planter dans le
cou de votre cheval. Celui-ci pousse un hennissement de douleur
puis s'abat en avant. Vous roulez tous deux dans la poussière du
chemin et vous vous retrouvez coincé sous le cadavre de votre
monture. Avant de fermer les yeux à jamais, vous avez le temps
de saisir une dernière vision : les fers de lance que les Gloks vous
auront, dans quelques secondes, enfoncés profondément dans la
poitrine. Votre mission a échoué.

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
