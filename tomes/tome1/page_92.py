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
                current_page_number=92)

fr_text = """
Vous plongez pour vous mettre à l'abri : il était temps, car une
pluie de flèches noires jaillies de la forêt s'abat en sifflant à
l'endroit où vous vous trouviez quelques secondes plus tôt. Vous
ramenez votre cape sur vos épaules : sa couleur verte vous
permet de vous fondre dans la végétation et vous vous mettez à
courir dans la forêt pour fuir le plus loin possible de vos
assaillants. Tous les environs sont infestés de Gloks, et il faut
vous échapper au plus vite. Vous courez sans vous arrêter
pendant plus d'une heure, et vous arrivez enfin sur un chemin
forestier qui mène droit vers l'est. Vous décidez de suivre ce
chemin en surveillant sans cesse les alentours de peur de voir
surgir un ennemi.
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
        st.page_link("tomes/tome1/page_13.py", label="13", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
