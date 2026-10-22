import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, has_item
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=9)

fr_text = """
Vous ne pouvez plus bouger : une force mystérieuse vous
immobilise et vos yeux sont attirés par la bouche du squelette.
Montant des profondeurs de la terre, vous entendez alors un
bourdonnement grave, comme si des millions d'abeilles en fureur
étaient rassemblées là. Puis une lueur rougeâtre s'allume dans les
orbites vides du roi mort et le bourdonnement augmente
d'intensité jusqu'à devenir assourdissant. Vous êtes en présence
d'une force maléfique plus ancienne et plus puissante encore que
celle des Maîtres des Ténèbres.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous possédez une Pierre de
Vordak, rendez-vous au"""
        )
    )
    if has_item("PIERRE PRÉCIEUSE"):
        fi = True
        if fi:
            st.page_link("pages/page_236.py", label="236", icon="📄")
    else:
        fi = True
        if fi:
            st.page_link("pages/page_236.py", label="236", icon="📄", disabled=True)

    st.write_stream(
        stream_text(f"""Sinon, rendez-vous au""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_292.py", label="292", icon="📄")



with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
