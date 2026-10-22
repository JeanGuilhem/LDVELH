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
                current_page_number=313)

fr_text = """
Vous essuyez votre Arme du sang fétide qui la souille et vous
vous hâtez de descendre le flanc de la colline avant que le Kraan
aperçoive les cadavres de ses cavaliers. A plusieurs reprises, vous
perdez l'équilibre, dégringolant de plusieurs mètres à la fois. Ces
chutes répétées occasionnent des écorchures et des contusions
qui vous coûtent 1 point d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    if st.session_state.last_page_number != st.session_state.current_page_number:
        st.session_state.endurance -= 1
        st.metric(label="Endurance", value=st.session_state.endurance, delta=-1)

    st.write_stream(
        stream_text(f"""Rendez-vous au:""")
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_248.py", label="248", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
