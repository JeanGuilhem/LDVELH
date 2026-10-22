
import streamlit as st
from inventory import display_inventory, check_inventory, end_page, pickup_button, pickup_gold, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=315)

fr_text = """
Enveloppé dans des vêtements de femme, vous trouvez un petit Sac de Velours qui contient 6 Pièces d'Or et un morceau de Savon Parfumé.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Vous pouvez prendre le Savon et l'Or en les inscrivant sur votre Feuille d'Aventure :"))
    pickup_gold(6)
    pickup_button("SAVON PARFUMÉ", key="soap", label="Prendre le Savon Parfumé")

    st.write_stream(
        stream_text(f"""Vous poursuivrez ensuite votre chemin. Rendez-vous au:""")
    )
    fi = True
    if fi:
        st.page_link("pages/page_213.py", label="213", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
