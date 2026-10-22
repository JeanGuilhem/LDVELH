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
                current_page_number=171)

fr_text = """
Vous avez atteint la lisière du bois lorsque votre cheval se cabre
soudain en poussant un hennissement de douleur. Le Kraan a
enfoncé ses serres pointues dans les pattes arrière de votre
monture et tente de vous désarçonner à grands coups d'aile.
Pendant ce temps, le Glok diabolique lance de petits cris
triomphants en brandissant sa lance. Vous sautez à terre et vous
courez vous mettre à l'abri parmi les arbres, laissant là votre
malheureux cheval qui agonise entre les griffes du Kraan.
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
        st.page_link("tomes/tome1/page_303.py", label="303", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
