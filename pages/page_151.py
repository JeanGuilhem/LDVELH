import streamlit as st
from inventory import display_inventory, check_inventory, add_to_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, set_cookies, called_cookies, handle_repas, ls_death, table_des_hasards



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

st.session_state.current_page_number = 151
check_inventory(is_fighting=False,
                current_page_number=st.session_state.current_page_number)

fr_text = """
En vous concentrant sur le trou de la serrure, vous pourrez peut-
être actionner le mécanisme interne et repousser le pêne par
votre seule force mentale. Vous ferez ensuite léviter la broche
pour la libérer de ses attaches. En opérant ainsi à distance, vous
resterez hors d'atteinte des pièges éventuels qui pourraient se
déclencher lors de l'ouverture de la serrure.
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
    if has_kai("Maîtrise Psychique de la Matière"):
        st.page_link("pages/page_87.py", label="87", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("pages/page_87.py", label="87", icon="📄", disabled=True)

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
