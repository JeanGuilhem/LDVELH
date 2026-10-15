
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
                current_page_number=289)

fr_text = """
Les deux soldats ont l'air fatigué et inquiet. Ils tiennent leur hallebarde devant eux, les mains crispées sur la hampe, et repoussent systématiquement quiconque veut s'approcher de la porte. Une femme en fureur attaque alors l'un d'eux, lui martelant la poitrine de ses poings, et le fait tomber sur l'autre garde. Tous trois s'écroulent aussitôt les uns sur les autres dans un enchevêtrement de bras et de jambes battant l'air en tous sens. C'est là votre chance, et vous vous précipitez vers la porte dont vous parvenez à déverrouiller les deux vantaux. Un instant plus tard, vous vous êtes glissé dans l'enceinte de la citadelle et vous vous retrouvez à l'entrée d'une cour intérieure. Tout a été si rapide qu'aucune des deux sentinelles ne vous a vu.
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
        st.page_link("pages/page_139.py", label="139", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
