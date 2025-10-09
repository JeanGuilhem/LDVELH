import streamlit as st
from inventory import display_inventory, check_inventory
from text import fr_unkown_kai
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=88)

fr_text = """
Vous jetez un regard prudent derrière le rocher et vous apercevez
un soldat étendu sur le dos, son épée et son bouclier à ses côtés.
Le bouclier porte l'image d'un Pégase blanc : c'est l'emblème du
Prince du Sommer-lund. Ce soldat appartient à la garde du
Prince ; son uniforme est déchiré et vous constatez qu'il porte au
bras une profonde blessure. Lorsque vous vous approchez de lui,
il bat des paupières. « Soignez-moi, supplie-t-il, je ne sens plus
mon bras. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            f"""Si vous maîtrisez la Discipline Kaï de la Guérison et
que vous désirez en faire bénéficier cet homme, rendez-vous au"""
        )
    )
    if "La Guérison" in list(st.session_state.kai.to_dict()["Mastery"].values()):
        fi = True
        if fi:
            st.page_link("pages/page_216.py", label="216", icon="📄")
    else:
        f_3 = True
        if f_3:
            st.write_stream(stream_text(fr_unkown_kai))
            st.page_link("pages/page_216.py", label="216", icon="📄", disabled=True)


    st.write_stream(
        stream_text(f"""Si vous ne maîtrisez pas cette Discipline, ou si vous ne
voulez pas en faire usage, rendez-vous au""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_31.py", label="31", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

