
import streamlit as st
from inventory import display_inventory, check_inventory, end_page, pickup_button
from utils import stream_text, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=290)

fr_text = """
A l'intérieur de la longue boîte, vous trouvez un Bâton enveloppé
de cuir. Vous pouvez le prendre si vous le désirez. Vous refermez
ensuite la boîte et vous redescendez l'échelle en prenant soin de
ne poser les pieds que sur les barreaux encore solides. Inscrivez,
le cas échéant, votre nouvelle Arme sur votre Feuille d'Aventure.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    pickup_button("BÂTON", key="staff", label="Prendre le Bâton")

    st.write_stream(
        stream_text(f"""Rendez-vous au:""")
    )
    fi = True
    if fi:
        st.page_link("pages/page_140.py", label="140", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
