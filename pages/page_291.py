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
                current_page_number=291)

fr_text = """
Les cadavres recroquevillés des deux Gloks reposent à vos pieds.
Le Kraan s'est enfui pendant le combat, et le sentier est à présent désert.
Vous calez votre Sac à Dos sur vos épaules et vous reprenez votre chemin.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            f"""Vous les fouillez rapidement et vous découvrez dans leurs
vêtements 6 Couronnes, 2 Lances et 1 Poignard. Vous pouvez
garder l'Or et prendre au choix le Poignard ou l'une des Lances.
Inscrivez dans ce cas votre nouvelle acquisition sur votre Feuille
d'Aventure."""
        )
    )

    pickup_gold(6)

    st.write("Vous pouvez prendre **une seule** de ces armes :")
    pickup_button("POIGNARD", key="weapon", label="Prendre le Poignard")
    pickup_button("LANCE", key="weapon", label="Prendre une Lance")

    st.write_stream(
        stream_text(f"""Rendez-vous au:""")
    )
    fi = True
    if fi:
        st.page_link("pages/page_272.py", label="272", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
