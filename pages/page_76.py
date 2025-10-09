import streamlit as st
from inventory import display_inventory, check_inventory, add_to_inventory
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=76)

fr_text = """
La Pierre dégage une intense chaleur et vous brûle la main. Vous
perdez 2 points d'ENDURANCE. Vous enveloppez alors la Pierre
dans un pan de votre cape et vous la laissez tomber dans une
poche de votre tunique. Une Pierre Précieuse de cette taille doit
valoir des centaines de Couronnes ! Vous vous réjouissez de votre
bonne fortune et vous remontez sur votre cheval que vous lancez
au galop sur le chemin orienté au sud.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.session_state.endurance -= 2
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)
    add_to_inventory(name="Pierre Précieuse")

    st.write_stream(
        stream_text(
            f"""Rendez-vous au """
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_118.py", label="118", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

