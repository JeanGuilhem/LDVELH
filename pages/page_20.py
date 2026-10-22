import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, pickup_button, show_illustrations
from utils import stream_text, set_cookies, called_cookies

if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=20)

fr_text = """
Il semble que le ou les occupants de la péniche soient partis en
toute hâte il y a peu de temps. Les restes d'un repas à moitié
mangé traînent sur la table ainsi qu'une tasse de Jala encore
chaud. En fouillant un coffre et un petit placard, vous trouvez un
Sac à Dos, de la Nourriture (l'équivalent de 2 Repas) et un
Poignard.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("SAC À DOS", key="1", label="Prendre le Sac à Dos")
    pickup_button("REPAS", key="2", label="Prendre un Repas")
    pickup_button("REPAS", key="3", label="Prendre un Repas")
    pickup_button("POIGNARD", key="4", label="Prendre le Poignard")

    st.write_stream(
        stream_text(
            f"""Rendez-vous ensuite au :"""
        )
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_272.py", label="272", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
