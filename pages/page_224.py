
import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    is_good = called_cookies()
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=224)

fr_text = """
Vous avez parcouru plusieurs kilomètres à cheval sans trouver
trace de réfugiés ou d'ennemis. Vous vous dirigez alors vers un
chemin qui s'élève un peu plus loin à flanc de colline. Sur cette
hauteur, vous devriez apercevoir la capitale. En arrivant là-haut,
vous contemplez en effet un spectacle qui vous remplit d'espoir,
mais qui vous fait frémir également : vous n'êtes décidément pas
au bout de vos peines...
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
        st.page_link("pages/page_153.py", label="153", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
