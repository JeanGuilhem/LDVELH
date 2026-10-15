import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai
from utils import stream_text, set_cookies, called_cookies

if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=111)

fr_text = """
Quelques minutes après avoir quitté le croisement, vous
apercevez un peu plus loin une petite cabane en rondins à côté
d'une écurie. Vous vous approchez et vous jetez un coup d'oeil
dans la cabane à travers le carreau d'une fenêtre. L'endroit
semble désert.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez entrer dans la cabane, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_57.py", label="57", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez inspecter l'écurie, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_308.py", label="308", icon="📄")

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
