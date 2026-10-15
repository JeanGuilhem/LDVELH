import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai
from text import fr_unkown_kai
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=71)

fr_text = """
Vous êtes étourdi, mais indemne. Vous avez fait une chute de
cinq mètres en passant à travers le plafond d'un caveau
souterrain. Les murs en sont parfaitement lisses, et il vous est
impossible d'y grimper. Un tunnel voûté part du caveau en
direction de l'est. A l'entrée de ce tunnel se trouve le sarcophage
de quelque ancien seigneur.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez ouvrir ce
sarcophage dans l'espoir d'y découvrir des objets de valeur,
rendez-vous au """
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_242.py", label="242", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez quitter le tombeau et
suivre le tunnel, rendez-vous au""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_104.py", label="104", icon="📄")

    st.write_stream(
        stream_text(
            f"""Enfin, si vous maîtrisez la Discipline Kaï du Sixième Sens, rendez-vous au:"""
        )
    )
    if has_kai("Le Sixième Sens"):
        st.page_link("pages/page_65.py", label="65", icon="📄")
    else:
        st.write_stream(
            stream_text(
                fr_unkown_kai
            )
        )
        st.page_link("pages/page_65.py", label="65", icon="📄", disabled=True)


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
