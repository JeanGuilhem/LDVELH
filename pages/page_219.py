import streamlit as st
from inventory import display_inventory, check_inventory, add_to_inventory, end_page, has_kai
from utils import stream_text, set_cookies, called_cookies, ls_death, handle_repas
from utils import table_des_hasards


if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    is_good = called_cookies()
    if not is_good:
        st.stop()

st.session_state.current_page_number = 219

check_inventory(is_fighting=False,
                current_page_number=st.session_state.current_page_number)

fr_text = """
Ce qui reste de vous se trouve encastré dans l'escalier, à une
profondeur de deux mètres, sous la masse d'un énorme bloc de
granité. Votre mission s'achève ici, en même temps que votre vie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    ls_death()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
