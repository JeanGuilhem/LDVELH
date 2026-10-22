import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, show_illustrations
from text import fr_unkown_kai
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=19)

fr_text = """
Un peu plus loin, à travers les arbres, vous apercevez des
buissons de couleur rouge. Ce sont des Brosses à Potence dont
les épines écarlates et pointues sont communément appelées des
Dents de Sommeil : elles ont en effet la propriété, lorsqu'on s'y
pique, de provoquer faiblesse et engourdissement.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text("Vous pouvez éviter les Dents de Sommeil en revenant sur le sentier. Rendez-vous alors au :")
    )
    st.page_link("tomes/tome1/page_272.py", label="272", icon="📄")

    st.write_stream(
        stream_text(
            "Vous pouvez au contraire essayer de vous frayer un chemin parmi ces buissons pour "
            "pénétrer plus profondément dans la forêt. Rendez-vous dans ce cas au :"
        )
    )
    st.page_link("tomes/tome1/page_119.py", label="119", icon="📄")

    st.write_stream(
        stream_text("Enfin, si vous maîtrisez la Discipline Kaï de l'Orientation, rendez-vous au :")
    )
    if has_kai("L'Orientation"):
        st.page_link("tomes/tome1/page_69.py", label="69", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome1/page_69.py", label="69", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
