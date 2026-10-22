
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
                current_page_number=264)

fr_text = """
Après avoir parcouru quelques centaines de mètres, vous entendez les échos d'une bataille qui fait rage un peu plus loin vers l'ouest.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez vous approcher de ce champ de bataille, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_97.py", label="97", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez poursuivre votre chemin en direction du sud, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_6.py", label="6", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
