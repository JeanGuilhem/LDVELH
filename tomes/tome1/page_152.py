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
                current_page_number=152)

fr_text = """
L'herboriste vous offre tout un choix de potions : certaines
d'entre elles accroissent votre force, d'autres vous rendent
invisible, d'autres encore vous donnent la faculté de vous faufiler
partout, et il en est même qui vous permettent de prendre une
forme gazeuse. Ensuite, l'homme ouvre un tiroir au bas de son
comptoir et vous montre une magnifique Baguette Magique.
D'après lui, il s'agit là d'une arme puissante qui vous permettra
de combattre efficacement toute créature malfaisante en vous
rendant vous-même invulnérable aux coups de vos adversaires.
Pour mieux vous en convaincre, il vous invite à lire une
inscription magique gravée sur la baguette.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez vous pencher par-dessus le comptoir pour lire l'étrange
inscription, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_49.py", label="49", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous vous intéressez davantage aux potions, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("tomes/tome1/page_231.py", label="231", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
