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
                current_page_number=332)

fr_text = """
Vous marchez pendant presque dix minutes le long d'un couloir
sombre et sinueux puis vous grimpez les marches d'un escalier
raide qui mène à une petite porte de bois. L'homme actionne
alors un loquet dissimulé aux regards et la porte s'ouvre. Vous
entrez peu après dans une grande pièce richement décorée : c'est
une chambre à coucher dont l'un des coins est occupé par une
immense baignoire de marbre. L'homme vous suggère de vous
rafraîchir pendant qu'il demande audience au Roi.
Vous prenez un bain rapide et vous revêtez une toge blanche
laissée là à votre intention sur une table de marbre. Quelques
minutes plus tard, l'homme revient et vous conduit le long d'un
couloir aux murs recouverts de luxueuses tapisseries. Vous
arrivez enfin devant une haute porte gardée par deux soldats
vêtus d'armures en argent. Dans quelques instants, vous serez
devant le Roi.
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
        st.page_link("pages/page_350.py", label="350", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
