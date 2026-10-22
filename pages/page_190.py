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
                current_page_number=190)

fr_text = """
Vous parcourez cinq kilomètres le long de la rivière et vous
découvrez alors une épave de péniche. Il semble que quelqu'un y
ait élu domicile car vous apercevez, au travers d'un trou dans le
pont, un lit et des ustensiles de cuisine.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous voulez fouiller cette péniche, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_20.py", label="20", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez poursuivre votre chemin, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_273.py", label="273", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
