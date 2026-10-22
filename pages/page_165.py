import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

st.session_state.current_page_number = 165

check_inventory(is_fighting=False,
                current_page_number=st.session_state.current_page_number)

fr_text = """
Vous vous réveillez tremblant de fièvre. Des images floues
défilent devant vos yeux puis s'effacent. Votre dos vous fait
terriblement mal et vous hurlez de douleur. Quelques instants
plus tard, vous sentez sur votre front le contact frais d'un linge
humide et vous apercevez à travers la brume de votre cerveau le
visage inquiet d'une jeune femme. Un vieillard lui murmure
quelque chose à l'oreille, puis disparaît de votre champ de vision.
La jeune fille s'agenouille alors près de vous et vous chuchote
quelques mots de réconfort, mais bientôt, la lumière s'évanouit à
nouveau et vous replongez dans les ténèbres. Rendez-vous au
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("pages/page_212.py", label="212", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
