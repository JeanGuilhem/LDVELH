
import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    is_good = called_cookies()
    if not is_good:
        st.stop()

st.session_state.current_page_number = 204
check_inventory(is_fighting=False,
                current_page_number=st.session_state.current_page_number)

fr_text = """
Après avoir marché pendant une heure, vous arrivez à une bifurcation. Le sentier que vous suivez continue vers le sud et un autre chemin sur votre droite part vers l'ouest. Le sentier orienté à l'ouest vous ramènerait droit au marécage et vous décidez donc de poursuivre en direction du sud.
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
        st.page_link("pages/page_111.py", label="111", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
