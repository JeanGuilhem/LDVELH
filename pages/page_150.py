import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

st.session_state.current_page_number = 150
check_inventory(is_fighting=False,
                current_page_number=st.session_state.current_page_number)

fr_text = """
Bien qu'elle soit un peu trop cuite, cette nourriture a un goût
délicieux (il n'y en a pas assez cependant pour constituer un
repas complet) et l'eau claire étanche votre soif. Vous avez passé
environ une demi-heure dans cette maison lorsque vous vous
rendez soudain compte que vous êtes en train de prendre du
retard. Ramassez vos affaires et reprenez votre chemin en vous
rendant au 83.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_83.py", label="83", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
