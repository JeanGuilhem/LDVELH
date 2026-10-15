
import streamlit as st
from inventory import display_inventory, check_inventory, end_page, pickup_button
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=305)

fr_text = """
Par la porte ouverte de la première hutte, vous apercevez le corps
d'un homme étendu face contre terre, sur le sol de pierre brute.
On l'a assassiné à l'aide d'une lance, sans aucun doute. Tous les
meubles et les objets que contenait la hutte ont été détruits : il ne
reste plus rien d'intact. Ce forfait porte la marque des Gloks : leur
goût du vandalisme est, en effet, bien connu. En entrant dans les
autres huttes, vous contemplez un spectacle semblable de
meurtre et de destruction. Dans la dernière hutte, vous
découvrez une Lance de Glok, ce qui confirme vos soupçons.
Vous pouvez la garder si vous le désirez en l'inscrivant sur votre
Feuille d'Aventure. Plus décidé que jamais à mener à bien votre
mission, vous poursuivez votre chemin le long du sentier.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write("Vous pouvez ajouter la Lance de Glok à votre inventaire :")
    pickup_button("LANCE DE GLOK", key="glok_spear", label="Prendre la Lance de Glok")

    st.write_stream(
        stream_text(
            f"""Rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_105.py", label="105", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
