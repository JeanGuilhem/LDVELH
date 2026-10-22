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
                current_page_number=48)

fr_text = """
Votre Sixième Sens vous avertit que ces soldats ne sont pas ce
qu'ils semblent être. Vous percevez une aura maléfique autour
d'eux : ce sont des serviteurs des Maîtres des Ténèbres. Il vous
faut prendre aussitôt la fuite avant qu'ils vous aperçoivent. 
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Rendez-vous au"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_243.py", label="243", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
