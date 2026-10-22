
import streamlit as st
from inventory import display_inventory, check_inventory, end_page, pickup_button, show_illustrations
from utils import stream_text, called_cookies


if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    is_good = called_cookies()
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=267)

fr_text = """
En vous couvrant le nez d'un pan de votre cape, vous vous approchez avec précaution du Kraan mort. L'odeur infecte qui se dégage de son sang noir vous retourne l'estomac, mais vous êtes décidé malgré tout à examiner son cadavre. Vous remarquez alors un sac attaché au corps du monstre par une sangle. A l'intérieur du sac, vous trouvez un Message écrit sur une peau d'animal. Tout au fond du sac, il y a également un Poignard. Vous pouvez conserver ce Message et ce Poignard si vous le désirez. Vous abandonnez ensuite le cadavre du monstre et vous poursuivez votre chemin en direction de l'est.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Vous pouvez ajouter les objets suivants à votre inventaire :"))

    pickup_button("MESSAGE", key="message", label="Prendre le Message")
    pickup_button("POIGNARD", key="dagger", label="Prendre le Poignard")

    st.write_stream(
        stream_text(
            f"""Rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_125.py", label="125", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
