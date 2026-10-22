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
                current_page_number=326)

fr_text = """
Vous introduisez avec précaution la Clé d'Or dans la serrure et
vous la tournez dans le sens des aiguilles d'une montre. Vous
entendez alors un faible déclic : le mécanisme a fonctionné. Vous
retirez ensuite la broche et la lourde porte de granité pivote
bientôt sur ses gonds, s'ouvrant vers vous. La lumière grise du
cimetière se diffuse dans le caveau et vous parvenez à sortir.
L'ouverture est, cependant, envahie de ronces et vous vous
écorchez le visage et les mains en vous hissant au-dehors.
Lorsque, enfin, vous vous retrouvez à l'air libre, la porte du
caveau se referme lentement derrière vous et un rire cruel,
inhumain, semble aussitôt s'élever des profondeurs de la terre,
juste sous vos pieds. Saisi de terreur, vous prenez vos jambes à
votre cou et vous vous précipitez vers la porte sud de la ville, en
traversant aussi vite que possible cette sinistre nécropole.
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
        st.page_link("pages/page_61.py", label="61", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
