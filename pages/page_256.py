
import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    is_good = called_cookies()
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=256)

fr_text = """
Vous êtes réveillé par des Kraans qui poussent leurs cris sinistres
dans le ciel bleu du matin. Vous vous frottez les yeux, puis vous
jetez un regard à travers les feuillages qui forment un dôme au-
dessus de vous : les répugnantes créatures volent en direction du
nord. Vous êtes sûr que les Kraans ne vous ont pas vu, mais vous
estimez préférable cependant, par simple prudence, de repartir
sans délai. Vous remontez donc sur votre cheval et vous galopez
sur la grand-route en direction du sud.
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
        st.page_link("pages/page_224.py", label="224", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
