import streamlit as st
from inventory import display_inventory, check_inventory, add_to_inventory
from utils import stream_text, set_cookies, called_cookies, before_fight, fight, handle_repas, ls_death


if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    is_good = called_cookies()
    if not is_good:
        st.stop()

current_page_number = 151
check_inventory(is_fighting=False,
                current_page_number=current_page_number)

fr_text = """
En vous concentrant sur le trou de la serrure, vous pourrez peut-être actionner le mécanisme interne et repousser le pêne par votre seule force mentale. Vous ferez ensuite léviter la broche pour la libérer de ses attaches. En opérant ainsi à distance, vous resterez hors d'atteinte des pièges éventuels qui pourraient se déclencher lors de l'ouverture de la serrure.
"""

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Pour savoir si votre Maîtrise Psychique de la Matière se révélera efficace dans le cas présent, rendez-vous au:"""
        )
    )
    if "Maîtrise Psychique de la Matière" in list(st.session_state.kai.to_dict()["Mastery"].values()):
        st.page_link("pages/page_87.py", label="87", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("pages/page_87.py", label="87", icon="📄", disabled=True)


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

st.session_state.last_page_number = st.session_state.current_page_number