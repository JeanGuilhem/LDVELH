import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    is_good = called_cookies()
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=262)

fr_text = """
Le marchand prend votre or et claque des doigts. Son garde du
corps vous attaque aussitôt.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez le combattre, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_191.py", label="191", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez éviter l'affrontement, vous
pouvez sauter en marche de la roulotte en vous rendant au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("tomes/tome1/page_234.py", label="234", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
