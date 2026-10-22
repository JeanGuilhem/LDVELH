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
                current_page_number=47)

fr_text = """
A bout de souffle et le visage ruisselant de sueur, vous vous
frayez un chemin vers le sommet de la colline. Mais, soudain,
une immense ombre noire se dessine devant vous : c'est un
Kraan qui tournoie dans le ciel tandis que les Gloks, dans votre
dos, gagnent peu à peu du terrain. 
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Souhaitez-vous attendre les
Gloks pour les affronter en prenant avantage de votre position
élevée ? Rendez-vous dans ce cas au"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_136.py", label="136", icon="📄")

    st.write_stream(
        stream_text(f"""Préférez-vous serrer
les dents et poursuivre l'escalade jusqu'au sommet ? Vous vous
rendrez alors au""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_322.py", label="322", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
