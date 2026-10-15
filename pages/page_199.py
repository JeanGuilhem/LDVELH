
import streamlit as st
from inventory import display_inventory, check_inventory, add_to_inventory, end_page, has_kai
from utils import stream_text, set_cookies, called_cookies, handle_repas, ls_death, table_des_hasards


if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=199)

fr_text = """
La plupart des placards et des tiroirs sont vides. Les habitants de
cette maison ont presque tout emporté avec eux ; vous parvenez
cependant à trouver dans la cave suffisamment de fruits pour
vous faire un Repas. Notez-le sur votre Feuille d'Aventure.
"""

if st.session_state.last_page_number != st.session_state.current_page_number:
    handle_repas()

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(f"""Rendez-vous ensuite au:""")
    )
    fi = True
    if fi:
        st.page_link("pages/page_81.py", label="81", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
