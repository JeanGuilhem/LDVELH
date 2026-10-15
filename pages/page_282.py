
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
                current_page_number=282)

fr_text = """
En portant votre regard au-delà de la foule, vous remarquez que l'une des boutiques qui font face à la Porte Principale est une officine de médecin. Un plan audacieux germe alors dans votre esprit. Vous vous frayez un chemin parmi la multitude et vous traversez la rue. Vous vous glissez ensuite dans la boutique du médecin : l'endroit semble désert à l'exception d'un perroquet aux vives couleurs enfermé dans une cage suspendue près de la vitrine. Vous enfilez rapidement une blouse blanche et vous ramassez quelques fioles de potions diverses, puis vous retraversez la rue jusqu'à la Porte Principale. « C'est pour une urgence ! vous exclamez-vous lorsque les sentinelles vous arrêtent à l'entrée. La femme du cuisinier du roi est sur le point d'accoucher ! » Les soldats hésitent un instant, mais vous affirmez qu'il s'agit bel et bien d'une urgence et ils finissent par vous laisser entrer. L'un des battants de la haute porte s'entrouvre d'une cinquantaine de centimètres et les gardes vous poussent d'un geste brusque par l'entrebâillement. Vous vous retrouvez alors dans la cour intérieure de la citadelle.
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
        st.page_link("pages/page_11.py", label="11", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
