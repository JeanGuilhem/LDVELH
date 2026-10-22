import streamlit as st
from inventory import display_inventory, check_inventory, end_page, pickup_button, receive_gold, show_illustrations
from utils import stream_text, called_cookies

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

    receive_gold(15)

    st.write("Vous pouvez ramasser la Clé d'Argent :")
    pickup_button("CLÉ D'ARGENT", key="silver_key", label="Prendre la Clé d'Argent (Objet Spécial)")

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

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
