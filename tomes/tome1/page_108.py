import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, set_cookies, called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=108)

fr_text = """
Tout semble se dérouler au ralenti tandis que vous décrivez dans
les airs un grand arc de cercle. Dans la rue au-dessous, vous
distinguez la foule qui grouille sur toute la largeur de la chaussée
et vous apercevez, sur votre droite, un nid de moineaux, blotti
dans une gouttière. Vous entendez alors leurs pépiements affolés
lorsque vous atterrissez avec fracas sur le toit d'en face. C'est
malheureusement la dernière chose que vous entendrez, car les
tuiles cèdent sous le choc et vous passez au travers des quatre
étages de l'Auberge de la Pantoufle Verte. Inutile de préciser que
vous vous êtes rompu le cou plusieurs fois et qu'il ne reste de
vous qu'un misérable petit tas de chair et d'os brisés.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Votre mission s'achève ici, en même temps que votre vie."""
        )
    )
    ls_death()

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
