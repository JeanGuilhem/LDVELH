
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
                current_page_number=241)

fr_text = """
Le sorcier entend votre cri et fait aussitôt volte-face, juste à
temps pour projeter un nouvel éclair en direction du Glok. La
tête de la créature explose aussitôt en une gerbe de flammes et
son corps s'écrase en un petit tas au pied de la colonne. Le chef
des Gloks vous voit et se met à hurler : « Groh gaï oh ! Groh gaï
oh ! » à ses troupes pour les inciter à repartir à l'attaque ; mais
les Gloks apeurés abandonnent bientôt les ruines pour courir se
réfugier dans la forêt. Le jeune sorcier s'essuie alors le front et
s'avance vers vous, la main tendue en signe de gratitude et
d'amitié.
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
        st.page_link("tomes/tome1/page_349.py", label="349", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
