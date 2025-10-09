import streamlit as st
from inventory import display_inventory, check_inventory
from utils import stream_text, set_cookies, called_cookies

if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=93)

fr_text = """
Vous faites volte-face et vous vous ruez vers l'escalier. Une
fraction de seconde plus tard, un énorme bloc de pierre s'écrase
sur le sol, juste dans votre dos. L'entrée de la pièce que vous
venez de quitter est, à présent, entièrement obstruée et, tandis
que vous vous précipitez au-dehors, vous apercevez derrière vous
la silhouette voûtée d'un vieux druide qui lève sa crosse. Un
instant plus tard, un éclair explose à vos pieds ; vous parvenez
cependant à l'éviter et vous descendez en courant le flanc de la
colline, furieux d'avoir perdu du temps, mais en remerciant votre
Sixième Sens de vous avoir sauvé la vie.
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
        st.page_link("pages/page_106.py", label="106", icon="📄")

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")