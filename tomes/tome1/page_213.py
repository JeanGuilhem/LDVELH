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
                current_page_number=213)

fr_text = """
Il y a bien deux heures à présent que vous vous frayez un chemin
dans la forêt et votre crainte de vous être perdu semble bel et
bien justifiée. Vous n'avez décelé aucune trace témoignant de la
présence de l'ennemi dans cette partie de la forêt ; seul le cri d'un
Kraan au lointain est venu parfois troubler la quiétude qui règne
alentour. Cependant, en descendant le flanc rocheux d'une petite
colline, vous remarquez soudain quelque chose d'insolite dans
l'enchevêtrement des sous-bois qui s'étendent devant vous.
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
        st.page_link("tomes/tome1/page_331.py", label="331", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
