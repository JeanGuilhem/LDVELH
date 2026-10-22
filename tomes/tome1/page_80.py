import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=80)

fr_text = """
Vous trébuchez en arrière et vous franchissez la porte d'entrée à
reculons, les mains crispées sur votre poitrine en feu. De la
fumée jaillit de la boutique et il vous faut prendre la fuite avant
que le Sage et son Voleur vous attrapent. Vous parvenez à
rejoindre la grand-rue et vous vous fondez dans la foule.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Rendezvous au"""
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_7.py", label="7", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
