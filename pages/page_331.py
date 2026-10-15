import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=331)

fr_text = """
Vous venez d'apercevoir l'entrée d'un tunnel qui disparaît dans
les profondeurs de la colline. L'ouverture du boyau est entourée
de ronces et de racines. Elle fait environ deux mètres de haut et
trois de large. En vous approchant, vous sentez une légère brise
souffler de ce vide d'un noir d'encre. Si l'autre extrémité du
tunnel aboutit au flanc opposé de la colline, vous pourriez vous
épargner de longues heures d'escalade en l'empruntant. Mais
vous prendriez alors le risque de vous exposer à quelque danger
inconnu.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez entrer dans ce tunnel, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_170.py", label="170", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez continuer à grimper vers le sommet de la colline, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_280.py", label="280", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
