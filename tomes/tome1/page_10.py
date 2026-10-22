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
                current_page_number=10)

fr_text = """
Vous êtes en sueur et vos jambes vous font mal. Un peu plus loin,
vous apercevez quelques maisonnettes rassemblées.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous
souhaitez entrer dans l'une de ces maisonnettes pour y prendre
quelque repos, rendez-vous au"""
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_115.py", label="115", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez poursuivre
votre chemin, rendez-vous au""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("tomes/tome1/page_83.py", label="83", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
