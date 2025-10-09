
import streamlit as st
from inventory import display_inventory, check_inventory
from utils import stream_text, set_cookies, called_cookies, ls_death
import random


if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=158)

fr_text = """
La clé s'adapte parfaitement à la serrure que vous n'avez aucun mal à ouvrir.
Vous faites pivoter la porte sur ses gonds et vous vous retrouvez face à face
avec un vieillard étrange qui porte un bâton à la main droite. Soudain, un éclair
jaillit du bâton et vous frappe en pleine poitrine. Vous perdez 6 points d'ENDURANCE.
Haletant de douleur, vous avez malgré tout (si vous n'êtes pas mort sur le coup)
la force de bousculer le vieil homme d'un coup d'épaule et de monter quatre à
quatre un escalier plutôt raide qui mène à la lumière du jour. Vous avez grimpé
la moitié des marches lorsque le vieillard fait jaillir un nouvel éclair de son bâton.
Utilisez la Table de Hasard pour obtenir un chiffre. Si vous tirez entre 0 et 5,
l'éclair vous rate et vient exploser contre le mur. Si vous tirez entre 6 et 9,
l'éclair vous frappe dans le dos et vous perdez 4 points d'ENDURANCE supplémentaires.
Si vous avez survécu, vous émergez à la lumière du jour en maudissant votre
mauvaise fortune. Vous avez découvert, par malchance, le temple secret d'une
secte de druides malfaisants et vous auriez pu tout aussi bien y laisser votre peau.
Vous vous hâtez à présent de rejoindre le sentier qui redescend de l'autre côté de la colline.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write_stream(stream_text(fr_text))

    if st.session_state.last_page_number != st.session_state.current_page_number:
        # First hit: -6 ENDURANCE
        st.session_state.endurance -= 6
        st.metric(label="Endurance", value=st.session_state.endurance, delta=-6)

        # Check for death after first hit
        if st.session_state.endurance <= 0:
            st.write_stream(stream_text("Votre mission s'achève ici."))
            ls_death()
            st.stop()

        # Dice roll and potential second hit
        roll_result = random.randint(0, 9)
        st.write_stream(stream_text(f"Vous lancez la Table de Hasard et obtenez un {roll_result}."))

        if roll_result >= 6:
            # Second hit: -4 ENDURANCE
            st.session_state.endurance -= 4
            st.metric(label="Endurance", value=st.session_state.endurance, delta=-4)

        # Check for death after second hit
        if st.session_state.endurance <= 0:
            st.write_stream(stream_text("Votre mission s'achève ici."))
            ls_death()
            st.stop()

    st.write_stream(
        stream_text(f"""Rendez-vous au:""")
    )
    fi = True
    if fi:
        st.page_link("pages/page_106.py", label="106", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

st.session_state.last_page_number = st.session_state.current_page_number
