import streamlit as st
from inventory import display_inventory, check_inventory, remove_from_backpack
from text import fr_unkown_kai
from utils import stream_text, set_cookies, called_cookies, handle_repas

if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=37)

fr_text = """
Vous vous sentez fatigué et affamé, et il vous faut faire une halte
pour prendre un Repas. Après avoir mangé, vous rebroussez
chemin jusqu'à la citadelle et vous marchez le long de ses hautes
murailles de pierre. Vous découvrez une autre entrée dans le mur
est, gardée, elle aussi, par deux soldats en armes.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    handle_repas()

    st.write_stream(
        stream_text(
            f""" Si vous voulez
vous approcher d'eux et leur raconter votre histoire, rendez-vous
au"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_289.py", label="289", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous maîtrisez la Discipline Kaï du Camouflage,
rendez-vous au""")
    )
    fi_1 = True
    if fi_1:
        if "Le Camouflage" in list(st.session_state.kai.to_dict()["Mastery"].values()):
            st.page_link("pages/page_282.py", label="282", icon="📄")
        else:
            st.write_stream(
                stream_text(
                    fr_unkown_kai
                )
            )
            st.page_link("pages/page_282.py", label="282", icon="📄", disabled=True)

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

