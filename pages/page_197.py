import streamlit as st
from inventory import display_inventory, check_inventory, end_page, pickup_button, pickup_gold
from utils import stream_text, called_cookies


if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=197)

fr_text = """
Le Drakkarim est étendu raide mort au fond de l'embarcation. Il
est porteur d'un sabre et de 6 Pièces d'Or que vous pouvez vous
approprier si tel est votre désir. Vous jetez ensuite le corps de
votre adversaire dans l'eau du lac et vous le regardez disparaître
dans ses profondeurs glacées. Vous ramassez ensuite la perche et
vous poussez le bateau sur l'autre rive où vous l'abandonnez.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write_stream(stream_text(fr_text))

    st.write_stream(stream_text("Vous pouvez prendre le sabre et les 6 Pièces d'Or :"))
    pickup_button("SABRE", key="sabre", label="Prendre le Sabre")
    pickup_gold(6)

    st.write_stream(
        stream_text(
            f"""Rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_172.py", label="172", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
