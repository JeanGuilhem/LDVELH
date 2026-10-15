import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=329)

fr_text = """
En descendant vers le Cimetière des Anciens, vous remarquez
une étrange brume qui baigne les lieux. Des nuages
tourbillonnent sur cette étendue grise, empêchant le soleil de
passer et maintenant la nécropole dans une obscurité
permanente. Vous sentez un frisson vous parcourir le corps
tandis que la température fraîchit peu à peu. Votre cheval se met
à regimber et vous avez beau l'éperonner, il refuse de s'approcher
de cet endroit sinistre. Il ne vous reste donc plus qu'à
abandonner votre monture pour continuer à pied.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_284.py", label="284", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
