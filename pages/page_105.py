import streamlit as st
from inventory import display_inventory, check_inventory
from utils import stream_text, set_cookies, called_cookies

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=105)

fr_text = """
Un peu plus loin, vous apercevez un Corbeau, d'un noir de jais,
perché sur la branche d'un vieux chêne.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    
    st.write_stream(
        stream_text(
            f"""Si vous maîtrisez la Discipline Kaï de la Communication Animale, vous pouvez
appeler cet oiseau en vous rendant au:"""
        )
    )
    if "Communication Animale" in list(st.session_state.kai.to_dict()["Mastery"].values()):
        st.page_link("pages/page_298.py", label="298", icon="📄")
    else:
        st.write_stream(
                stream_text(
                        fr_unkown_kai
                )
        )
        st.page_link("pages/page_298.py", label="298", icon="📄", disabled=True)

    st.write_stream(
        stream_text(f"""Sinon, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_335.py", label="335", icon="📄")

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")