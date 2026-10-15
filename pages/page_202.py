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
                current_page_number=202)

fr_text = """
Vous galopez le long de la grand-route qui mène à la capitale
lorsque votre cheval ralentit soudain l'allure, se met à boiter, puis
s'arrête. Vous mettez pied à terre pour examiner sa jambe avant
droite qu'il tient levée : il a perdu un fer et s'est blessé au sabot.
En maudissant votre mauvaise fortune, vous l'abandonnez donc
sur le bas-côté et vous poursuivez à pied votre chemin.
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
        st.page_link("pages/page_58.py", label="58", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
