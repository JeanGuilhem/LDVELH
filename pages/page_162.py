import streamlit as st
from inventory import (
    display_inventory,
    check_inventory,
    end_page,
    has_kai,
    is_new_page,
    lose_all_weapons,
    lose_backpack,
)
from utils import stream_text, called_cookies
from text import fr_unkown_kai

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=162)

fr_text = """
Vous vous approchez de ces hommes et vous les appelez. Mais
lorsqu'ils se tournent vers vous, votre sang se glace et vous sentez
votre cœur battre à tout rompre, car ce sont des Drakkarims
déguisés. En vous voyant, ils se précipitent sur vous, vous
ligotent pieds et poignets et vous traînent derrière eux le long
d'un sentier. Ils vous prennent votre Sac à Dos et vos Armes,
mais ils ne fouillent pas les poches de votre cape et ne trouvent
pas vos Pièces d'Or. Vous les entendez jacasser d'un air menaçant
tandis qu'ils vous emportent ainsi vers leur repaire : de toute
évidence, ils sont en train de décider du sort qu'ils vous
réservent, et vos perspectives d'avenir ne semblent pas des plus
réjouissantes.
"""

if is_new_page():
    lose_backpack()
    lose_all_weapons()

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Si vous possédez la Discipline Kaï de la Maîtrise Psychique de la Matière, rendez-vous au :"
        )
    )
    if has_kai("Maîtrise Psychique de la Matière"):
        st.page_link("pages/page_258.py", label="258", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("pages/page_258.py", label="258", icon="📄", disabled=True)

    st.write_stream(stream_text("Sinon, rendez-vous au :"))
    if has_kai("Maîtrise Psychique de la Matière"):
        st.page_link("pages/page_127.py", label="127", icon="📄", disabled=True)
    else:
        st.page_link("pages/page_127.py", label="127", icon="📄")

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
