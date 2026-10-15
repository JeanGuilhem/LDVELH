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
                current_page_number=166)

fr_text = """
Vous êtes en présence d'une force hautement maléfique. Un être
puissant et invisible essaie de soumettre votre esprit, et il vous
faut rassembler toute votre énergie pour vous défendre. Cette
lutte intense vous met en grand danger de perdre la raison. Vous
traversez une longue et pénible épreuve au cours de laquelle
toutes sortes d'apparitions terrifiantes, surnaturelles,
fantasmagoriques essaient de vous attirer dans leur monde de
folie. La tentation et l'horreur se mélangent dans votre tête et ce
n'est qu'à grand-peine que vous parvenez à sortir vainqueur de ce
véritable calvaire.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if st.session_state.last_page_number != st.session_state.current_page_number:
        st.session_state.endurance -= 4
        st.metric(label="Endurance", value=st.session_state.endurance, delta=-4)

    st.write_stream(
        stream_text(
            f"""Vous perdez 4 points d'ENDURANCE et vous entrez dans le tunnel d'un pas chancelant. Rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_104.py", label="104", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
