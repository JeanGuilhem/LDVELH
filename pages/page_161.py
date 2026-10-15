
import streamlit as st
from inventory import display_inventory, check_inventory, add_to_inventory, end_page, has_kai
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=161)

fr_text = """
Au moment où vous vous asseyez, le Serpent de Pierre se met à bouger. Une sueur froide perle à votre front et vous empoignez votre arme d'une main tremblante, prêt à vous défendre contre une attaque éventuelle. Une langue rouge et fourchue jaillit alors de la tête de cette étrange statue et vient plonger dans la coupe de lumière verte posée sur le dossier du trône, au-dessus de vous. Lentement, la langue fourchue ressort de la coupe en tenant une Clé d'Or qu'elle laisse tomber sur vos genoux. Un instant plus tard, un panneau glisse dans le mur est de la pièce, découvrant l'entrée d'un passage secret. Vous prenez la Clé et vous vous hâtez de quitter les lieux par cette sortie inattendue.
"""

if st.session_state.last_page_number != st.session_state.current_page_number:
    add_to_inventory(name="Clé d'Or")
    st.success("Vous avez ajouté la Clé d'Or à votre inventaire.")


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
        st.page_link("pages/page_209.py", label="209", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
