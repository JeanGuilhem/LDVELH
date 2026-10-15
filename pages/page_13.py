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
                current_page_number=13)

fr_text = """
Le chemin aboutit bientôt à une vaste clairière. En son centre se
dresse un arbre plus haut et plus large que les autres. Nichée
dans son feuillage, à quelque huit mètres au-dessus du sol, se
trouve une grande maison. Aucune échelle ne permet d'y
accéder, mais l'écorce noueuse de l'arbre offre de nombreux
points d'appui et il ne doit pas être trop difficile de grimper là-
haut.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""
            Si vous souhaitez escalader cet arbre pour inspecter la
maison, rendez-vous au
"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_307.py", label="307", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez poursuivre votre
chemin, rendez-vous au""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_213.py", label="213", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
