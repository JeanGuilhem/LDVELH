import streamlit as st
from inventory import display_inventory, check_inventory, end_page, change_endurance
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=36)

fr_text = """
Le bois de l'échelle qui monte à la vieille tour de guet, est pourri
et plusieurs barreaux cèdent sous votre poids.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    number = hazard_roll()
    if number is not None and number <= 4:
        if "hazard_fall_done" not in st.session_state:
            st.session_state["hazard_fall_done"] = True
            change_endurance(-2)
        st.write_stream(stream_text("Vous tombez et vous perdez 2 points d'ENDURANCE."))
        st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)
        st.page_link("pages/page_140.py", label="140", icon="📄")
    elif number is not None:
        st.write_stream(stream_text("Vous ne tombez pas."))
        st.page_link("pages/page_323.py", label="323", icon="📄")

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
