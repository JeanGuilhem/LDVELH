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
                current_page_number=67)

fr_text = """
Votre Sens de l'Orientation vous permet de découvrir des traces
fraîches laissées par les pattes d'un animal. Ces empreintes
suivent le chemin orienté au sud. Vous reconnaissez là les traces
d'un Ours Noir. C'est un animal connu pour sa férocité et vous
estimez préférable d'emprunter le sentier qui mène vers l'est.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome1/page_140.py", label="140", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
