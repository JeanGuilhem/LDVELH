
import streamlit as st
from inventory import display_inventory, check_inventory, end_page, pickup_button, show_illustrations
from utils import stream_text, called_cookies


if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=164)

fr_text = """
Vous débouchez prudemment chacune des bouteilles et vous
reniflez son contenu. Il semble s'agir là de différentes sortes de
vin. Mais soudain, une autre bouteille, plus petite, coincée parmi
les autres, attire votre attention. Elle est remplie d'un liquide de
couleur orange dont l'odeur vous est familière : c'est de l'Essence
d'Alether, une puissante potion qui a la propriété d'accroître
votre force. Vous pouvez conserver cette fiole et en boire le
contenu au début d'un combat : votre total d'HABILETÉ
augmentera alors de 2 points pendant toute la durée de
l'affrontement. Cette quantité d'essence d'Alether ne représente
qu'une seule dose, vous ne pourrez donc en faire usage qu'une
fois. Inscrivez cette Potion dans la case Objets Spéciaux de votre
Feuille d'Aventure, et n'oubliez pas de l'effacer lorsque vous
l'aurez bue.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Vous pouvez ajouter l'Essence d'Alether à votre inventaire :"))
    pickup_button("ESSENCE D'ALETHER", key="alether", label="Prendre l'Essence d'Alether")

    st.write_stream(
        stream_text(f"""Vous décidez à présent d'inspecter l'écurie en vous rendant au:""")
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_308.py", label="308", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
