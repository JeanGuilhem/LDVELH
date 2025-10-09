import streamlit as st
from inventory import display_inventory, check_inventory
from utils import stream_text, set_cookies, called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=60)

fr_text = """
Avant que les ténèbres vous engloutissent, vous apercevez l'éclat
d'une longue lame de couteau. Votre nom s'ajoutera à la liste des
victimes du Sage et de son fils, le Voleur, celui-là même qui vient
de vous trancher la gorge. Votre mission est terminée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    ls_death()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

