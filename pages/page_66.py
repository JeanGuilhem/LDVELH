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
                current_page_number=66)

fr_text = """
Surpris, vous faites volte-face et vous voyez courir vers vous un
robuste sergent accompagné de deux soldats. Tous trois
brandissent leurs épées, prêts à frapper. A votre tour, vous
dégainez votre arme car, apparemment, ils vont vous attaquer
sans prendre la peine de poser des questions. Mais, soudain, le
sergent ordonne à ses hommes de s'arrêter. Il a, en effet, reconnu
votre cape de Seigneur Kaï. Tous trois remettent aussitôt leurs
épées au fourreau et se confondent en excuses. Le sergent vous
accompagne ensuite vers l'Entrée Principale et envoie un de ses
hommes chercher le capitaine de la garde. Vous êtes bientôt
accueilli par un soldat de haute taille et de belle allure qui écoute
attentivement votre récit. Lorsque vous avez fini de lui raconter
votre périlleux voyage jusqu'à la capitale, vous remarquez qu'il a
les larmes aux yeux. Il vous demande alors de le suivre et vous
parcourez les salons et les couloirs somptueux du palais royal.
Tout ici n'est que splendeur et magnificence. Enfin, vous arrivez
devant une haute porte sculptée gardée par deux soldats revêtus
d'armures en argent. Dans quelques instants, vous serez devant
le Roi.
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
        st.page_link("pages/page_350.py", label="350", icon="📄")



with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

