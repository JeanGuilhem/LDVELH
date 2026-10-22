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
                current_page_number=121)

fr_text = """
Après quelques minutes de marche, vous apercevez la silhouette
d'un homme vêtu de rouge qui se tient debout au milieu du
chemin. Il vous tourne le dos, et un capuchon lui couvre la tête.
Le corbeau noir que vous avez vu un peu plus tôt est perché sur
son bras tendu.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez appeler cet homme, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_342.py", label="342", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez vous approcher de lui avec prudence, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("tomes/tome1/page_309.py", label="309", icon="📄")

    st.write_stream(
        stream_text(
            f"""Enfin, si vous estimez plus judicieux de dégainer votre arme et de l'attaquer, rendez-vous au:"""
        )
    )
    fi_2 = True
    if fi_2:
        st.page_link("tomes/tome1/page_283.py", label="283", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
