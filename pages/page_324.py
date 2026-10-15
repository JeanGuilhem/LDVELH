
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
                current_page_number=324)

fr_text = """
Vous rabattez votre capuchon sur votre tête et vous vous laissez
tomber derrière les monticules de pierre qui s'entassent devant
l'entrée de la grotte. Retenant votre souffle, vous vous roulez en
boule en vous recouvrant entièrement de votre cape verte de
Seigneur Kaï. Quelques minutes plus tard, les Gloks grimpent sur
l'amas de pierres et scrutent de leurs petits yeux jaunes chaque
crevasse qui s'ouvre au flanc de la colline. Puis, lançant force
jurons dans leur étrange dialecte, ils redescendent du tas de
pierres et poursuivent leur ascension en direction du sommet de
la colline. Vous remerciez alors silencieusement vos Maîtres Kaï
de vous avoir enseigné la Science du Camouflage, car la mise en
pratique de cette discipline vient probablement de vous sauver la
vie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez explorer la grotte, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_33.py", label="33", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez quitter les lieux et redescendre le flanc de la colline
de peur que les Gloks ne reviennent, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_248.py", label="248", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
