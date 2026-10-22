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
                current_page_number=16)

fr_text = """
Vous parvenez à détacher l'un des chevaux de la roulotte. L'odeur
des Loups Maudits et les cris des Gloks qui les chevauchent
semblent l'effrayer, mais vous arrivez malgré tout à le lancer au
galop en direction des monstrueuses créatures qui s'approchent
de vous. Les Gloks et leurs montures sataniques ne sont plus qu'à
une cinquantaine de mètres, la lance pointée en avant. Face à
face à présent, vous foncez les uns vers les autres.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Rendez-vous
au"""
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_192.py", label="192", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
