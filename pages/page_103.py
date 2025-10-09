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
                current_page_number=103)

fr_text = """
Le chemin, couvert de broussailles, bifurque bientôt et un autre
sentier permet d'aller vers l'est.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez emprunter ce nouveau chemin orienté à l'est, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_13.py", label="13", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez poursuivre votre route en direction du nord-est, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_287.py", label="287", icon="📄")

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")
