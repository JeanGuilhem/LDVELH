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
                current_page_number=57)

fr_text = """
La cabane n'a qu'une seule pièce meublée d'une table de bois, de
deux bancs et d'un lit fait de bottes de paille attachées ensemble.
Un tapis brodé orne le plancher et plusieurs bouteilles contenant
des liquides de différentes couleurs sont posées sur la table.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si
vous souhaitez examiner ces bouteilles, rendez-vous au"""
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_164.py", label="164", icon="📄")

    st.write_stream(
        stream_text(f""" Si
vous voulez soulever le tapis, rendez-vous au""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("tomes/tome1/page_109.py", label="109", icon="📄")

    st.write_stream(
        stream_text(
            f"""Si vous
préférez quitter la cabane et inspecter l'écurie, rendez-vous au"""
        )
    )
    fi_2 = True
    if fi_2:
        st.page_link("tomes/tome1/page_308.py", label="308", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
