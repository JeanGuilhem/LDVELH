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
                current_page_number=218)

fr_text = """
Votre Sixième Sens vous indique que ce ne sont pas seulement
des chevaux qui galopent dans votre direction. Vous percevez
également la cavalcade d'une meute de Loups Maudits et des cris
de guerre poussés par des Gloks. D'après l'intensité de ces
hurlements, vous jugez qu'il doit y avoir là plus d'une douzaine
de Gloks et il est donc préférable de ne pas manifester votre
présence, pour l'instant tout au moins.
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
        st.page_link("tomes/tome1/page_75.py", label="75", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
