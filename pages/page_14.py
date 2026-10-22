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
                current_page_number=14)

fr_text = """
Vous parvenez au sommet d'une petite colline boisée. De gros
rocs y sont disposés les uns à côté des autres, formant un cercle
grossier. Soudain, vous entendez un grognement sonore qui
s'élève de derrière un rocher situé à votre gauche.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous voulez
dégainer votre arme et vous préparer à combattre, rendez-vous au"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_43.py", label="43", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez prendre la fuite en courant le plus vite
possible au bas de la colline, rendez-vous au""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_106.py", label="106", icon="📄")

    show_illustrations()



with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
