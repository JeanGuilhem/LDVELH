
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
                current_page_number=348)

fr_text = """
D'un coup de pied, vous jetez au loin le corps du serpent et vous
êtes alors saisi d'une terreur rétrospective, car cette Vipère des
Marais était une vipère rouge et aucun remède n'existe contre la
puissance de son venin ! Vous estimez qu'il serait suicidaire de
continuer plus avant dans cette direction et vous revenez donc
sur vos pas jusqu'à ce que vous retrouviez un terrain plus ferme.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Vous poursuivez ensuite votre chemin en vous rendant au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_95.py", label="95", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
