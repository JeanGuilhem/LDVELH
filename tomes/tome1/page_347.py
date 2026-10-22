import streamlit as st
from inventory import display_inventory, check_inventory, end_page, pickup_button, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=347)

fr_text = """
La forêt s'éclaircit bientôt et vous apercevez un peu plus loin une vieille cabane en rondins, construite sous un chêne. La cabane semble avoir été abandonnée et il n'y reste apparemment rien de très intéressant. En ouvrant un petit coffre posé près de la porte, vous découvrez des fagots de branches liées ensemble avec de la ficelle. Les fagots ont été enduits de poix à l'une de leurs extrémités : ils peuvent ainsi faire office de Torches. Près du coffre, vous trouvez également un Sabre et un Briquet à Amadou. Vous pouvez les prendre ainsi qu'une des Torches, à condition, bien entendu, de modifier en conséquence votre Feuille d'Aventure. Vous refermez ensuite la porte de la cabane et vous poursuivez votre chemin le long d'un sentier recouvert de broussailles et orienté au nord-est.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Vous pouvez ajouter les objets suivants à votre inventaire :"))

    pickup_button("TORCHE", key="torch", label="Prendre une Torche")
    pickup_button("SABRE", key="sabre", label="Prendre le Sabre")
    pickup_button("BRIQUET À AMADOU", key="tinderbox", label="Prendre le Briquet à Amadou")

    st.write_stream(
        stream_text(
            f"""Rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_103.py", label="103", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
