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
                current_page_number=273)

fr_text = """
Les fortifications du camp militaire dressé autour de la ville vous
apparaissent un peu plus loin. Des péniches amarrées les unes
aux autres sont alignées en travers du cours d'eau, formant ainsi
une barricade flottante. Vous apercevez également des soldats
qui courent le long des fortifications et vous entendez, en
provenance de l'ouest, les échos lointains d'une bataille.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous voulez vous approcher de ces péniches, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_179.py", label="179", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez vous cacher à l'abri des arbres, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_51.py", label="51", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
