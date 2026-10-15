import streamlit as st
from inventory import display_inventory, check_inventory, end_page, change_endurance, is_new_page
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=158)

if is_new_page():
    change_endurance(-6)

fr_text = """
La clé s'adapte parfaitement à la serrure que vous n'avez aucun
mal à ouvrir. Vous faites pivoter la porte sur ses gonds et vous
vous retrouvez face à face avec un vieillard étrange qui porte un
bâton à la main droite. Soudain, un éclair jaillit du bâton et vous
frappe en pleine poitrine. Vous perdez 6 points d'ENDURANCE.
Haletant de douleur, vous avez malgré tout (si vous n'êtes pas
mort sur le coup) la force de bousculer le vieil homme d'un coup
d'épaule et de monter quatre à quatre un escalier plutôt raide qui
mène à la lumière du jour. Vous avez grimpé la moitié des
marches lorsque le vieillard fait jaillir un nouvel éclair de son
bâton.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-6)

    number = hazard_roll()
    if number is not None and number <= 5:
        st.write_stream(stream_text("L'éclair vous rate et vient exploser contre le mur."))
    elif number is not None:
        if "hazard_second_bolt_done" not in st.session_state:
            st.session_state["hazard_second_bolt_done"] = True
            change_endurance(-4)
        st.write_stream(
            stream_text(
                "L'éclair vous frappe dans le dos et vous perdez 4 points d'ENDURANCE supplémentaires."
            )
        )
        st.metric(label="Endurance", value=st.session_state.endurance, delta=-4)

    if number is not None:
        st.write_stream(
            stream_text(
                "Vous émergez à la lumière du jour en maudissant votre mauvaise fortune. "
                "Vous avez découvert, par malchance, le temple secret d'une secte de druides "
                "malfaisants et vous auriez pu tout aussi bien y laisser votre peau. Vous vous "
                "hâtez à présent de rejoindre le sentier qui redescend de l'autre côté de la colline."
            )
        )
        st.page_link("pages/page_106.py", label="106", icon="📄")

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
