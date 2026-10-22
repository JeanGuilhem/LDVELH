
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
                current_page_number=330)

fr_text = """
Vaincu par la fatigue, vous vous arrêtez bientôt devant un arbre
mort sur lequel vous vous asseyez pour prendre quelque repos.
Vous remarquez alors, coincé sous le tronc, un gros paquet ficelé
comme un baluchon.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez examiner le contenu de ce paquet, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_315.py", label="315", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez le laisser où il est et poursuivre votre chemin dès que vous vous sentirez un peu reposé, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_213.py", label="213", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
