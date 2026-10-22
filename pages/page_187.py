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
                current_page_number=187)

fr_text = """
Deux têtes au pelage ras apparaissent derrière le tronc. Les deux
créatures jettent un coup d'œil à votre arme et poussent un cri
d'effroi. Elles bondissent alors loin du tronc et s'enfuient dans la
forêt.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez vous lancer à leur poursuite, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_186.py", label="186", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez les laisser partir et continuer votre chemin, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_228.py", label="228", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
