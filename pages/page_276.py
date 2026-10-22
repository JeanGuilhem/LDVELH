import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

current_page_number = 276
check_inventory(is_fighting=False,
                current_page_number=current_page_number)

fr_text = """
Vous empoignez votre Hache et vous vous frayez un chemin dans
l'enchevêtrement de racines et de branches noueuses qui obstrue
le chemin. Bientôt, votre cape est déchirée en plusieurs endroits
et votre jambe droite douloureusement meurtrie, juste au-dessus
du genou.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    if st.session_state.last_page_number != st.session_state.current_page_number:
        st.session_state.endurance -= 1
        st.metric(label="Endurance", value=st.session_state.endurance, delta=-1)

    st.write_stream(
        stream_text(
            f"""Vous perdez 1 point d'ENDURANCE avant de vous rendre au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_213.py", label="213", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
