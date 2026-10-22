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
                current_page_number=284)

fr_text = """
Votre traversée du Cimetière n'ira pas sans difficultés, car le sol
en est inégal et recouvert de broussailles épineuses qui déchirent
votre cape et vous écorchent les jambes. L'air est lourd et
immobile, des vapeurs pestilentielles s'exhalent des cryptes
entrouvertes et un murmure lancinant parvient faiblement
jusqu'à vous, une sorte de chuchotement ininterrompu, venu de
nulle part et de partout à la fois. Vous vous approchez avec
précaution d'un espace ouvert entre deux anciennes colonnes et
vous écartez les broussailles en ayant pris soin d'envelopper vos
mains dans un pan de votre cape. Or, soudain, le sol se dérobe
sous vos pas et vous tombez en quelque mystérieuse profondeur
dans un éboulement de terre et de cailloux.
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
        st.page_link("pages/page_71.py", label="71", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
