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
                current_page_number=70)

fr_text = """
Vous arrivez à un petit pont. Un chemin longe le cours d'eau en
direction de l'est, et un autre sentier beaucoup plus étroit
s'enfonce dans une forêt touffue menant vers le sud.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous
souhaitez aller à l'est, rendez-vous au """
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_28.py", label="28", icon="📄")

    st.write_stream(
        stream_text(f""" Si vous préférez
prendre la direction du sud, rendez-vous au""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_157.py", label="157", icon="📄")

    st.write_stream(
        stream_text(
            f"""Enfin, si vous
maîtrisez la Discipline Kaï du Sixième Sens, rendez-vous au"""
        )
    )
    if has_kai("Le Sixième Sens"):
        st.page_link("pages/page_8.py", label="8", icon="📄")
    else:
        st.write_stream(
            stream_text(
                fr_unkown_kai
            )
        )
        st.page_link("pages/page_8.py", label="8", icon="📄", disabled=True)


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
