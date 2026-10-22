import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

st.session_state.current_page_number = 174
check_inventory(is_fighting=False,
                current_page_number=st.session_state.current_page_number)

fr_text = """
Après vous être laissé dériver pendant environ une heure, vous
remarquez que le courant devient plus fort. Vous apercevez alors
à quelque distance un tourbillon que forment les eaux de la
rivière à hauteur d'un méandre. Les flots vous entraînent vers ce
puissant remous qui pourrait bien signifier pour vous la noyade
pure et simple. Il ne vous reste plus qu'à plonger dans les eaux
boueuses pour regagner la berge. Malheureusement, tandis que
vous nagez en vous éloignant du courant, votre Sac à Dos se
détache et tombe au fond de l'eau ainsi que vos Armes. C'est
donc privé de votre équipement que vous atteignez la rive boisée
sur laquelle vous parvenez à vous hisser tant bien que mal.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if st.session_state.last_page_number != st.session_state.current_page_number:
        st.session_state.inventory = [] # Lose all equipment (backpack and weapons)
        st.info("Votre Sac à Dos et vos Armes sont tombés au fond de l'eau. Votre inventaire a été vidé de ces objets.")

    st.write_stream(
        stream_text(
            f"""Rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_190.py", label="190", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
