import streamlit as st
from inventory import display_inventory, check_inventory
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=141)

fr_text = """
Votre Sixième Sens vous avertit que quelques-unes des créatures
qui ont attaqué le monastère sont restées dans les environs et
inspectent les deux chemins, en quête d'éventuels survivants à
massacrer. Vous pouvez cependant éviter ces deux sentiers en
coupant par les sous-bois de la forêt.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez aller vers le sud, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_56.py", label="56", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez vous frayer un chemin dans le feuillage plus touffu qui s'étend au nord-est, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_333.py", label="333", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

st.session_state.last_page_number = st.session_state.current_page_number