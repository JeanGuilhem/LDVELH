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
                current_page_number=163)

fr_text = """
Au bout d'une demi-heure environ, vous sentez que le courant
devient plus fort. Un peu plus loin, le cours de la rivière forme un
méandre et ses eaux s'agitent en un puissant tourbillon qui vous
emportera au fond si vous vous laissez entraîner. Vous décidez
donc de nager vers la rive droite et de poursuivre votre chemin à
pied. Votre équipement est au complet, vous n'avez rien perdu
dans les eaux de la rivière.
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
        st.page_link("pages/page_321.py", label="321", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
