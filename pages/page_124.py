import streamlit as st
from inventory import display_inventory, check_inventory, add_to_inventory
from utils import stream_text, set_cookies, called_cookies

if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    is_good = called_cookies()
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=124)

fr_text = """
Dans la boîte, vous trouvez 15 Pièces d'Or et une Clé d'Argent. Si
vous souhaitez conserver la Clé, inscrivez-la sur votre Feuille
d'Aventure dans la case Objets Spéciaux.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if st.session_state.last_page_number != st.session_state.current_page_number:
        st.session_state.purse += 15
    st.metric(label="Couronnes", value=st.session_state.purse, delta=+15)

    st.write("Vous pouvez ramasser la Clé d'Argent :")
    if st.button(label="Clé d'Argent (Objet Spécial)", key="cle_argent_124", disabled=st.session_state.visibility_1):
        st.session_state.visibility_1 = True
        add_to_inventory(name="CLE D'ARGENT")
        st.info("Clé d'Argent ajoutée à votre inventaire.")
        st.rerun()
        
    st.write_stream(
        stream_text(
            f"""Vous pouvez continuer à explorer le tunnel en vous rendant au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_211.py", label="211", icon="📄")

    st.write_stream(
        stream_text(f"""Vous pouvez également descendre le flanc de la colline en vous rendant au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_106.py", label="106", icon="📄")

    # SAUVEGARDE DE LA PAGE ACTUELLE POUR LES FUTURS RE-RUNS
    st.session_state.last_page_number = st.session_state.current_page_number

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")