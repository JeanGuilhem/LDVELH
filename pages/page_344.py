
import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    is_good = called_cookies()
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=344)

fr_text = """
Vous vous sentez faible et vous avez le tournis. Vos jambes
deviennent insensibles et se refusent à porter votre poids. Vous
essayez d'atteindre la porte, mais le voleur se rue sur vous et vous
plaque au sol.
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
        st.page_link("pages/page_60.py", label="60", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
