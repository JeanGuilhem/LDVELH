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
                current_page_number=82)

fr_text = """
Le Gourgaz Géant est étendu à vos pieds ; ses compagnons
sifflent de rage en vous lançant des regards furieux, puis ils
sautent du pont. Les tirs de flèches reprennent de plus belle
tandis que les soldats du Prince forment autour de vous et de
leur chef agonisant un mur de protection à l'aide de leurs
boucliers. Le Prince moribond vous regarde alors dans les yeux
et prononce ces derniers mots : « Seigneur Kaï, il vous faut
transmettre un message au Roi, mon père. L'ennemi est trop
puissant, nous ne pouvons le contenir. C'est à Durenor que se
trouve notre salut; Sa Majesté doit envoyer chercher ce qui peut
nous épargner la défaite. Mon père comprendra ce que je veux
dire. Prenez mon cheval et gagnez la capitale. Puissent les Dieux
vous accompagner au long de votre voyage ! » Le cœur plein de
tristesse, vous dites alors adieu au Prince, puis vous enfourchez
son étalon blanc que vous lancez au galop en direction du sud, le
long du chemin forestier. Derrière vous, l'ennemi repart à
l'assaut du pont et les échos d'une féroce bataille retentissent
encore longtemps à vos oreilles.
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
        st.page_link("pages/page_235.py", label="235", icon="📄")

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

