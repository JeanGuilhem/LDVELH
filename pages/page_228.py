import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    is_good = called_cookies()
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=228)

fr_text = """
Le sentier continue vers l'est puis disparaît bientôt sous
d'épaisses broussailles.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez poursuivre vers l'est en vous frayant un chemin à coups de hache, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_140.py", label="140", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez aller vers le sud, là où les sous-bois sont moins touffus et vous enfoncer plus avant dans la forêt, rendez-vous au:""")
    )
    st.page_link("pages/page_215.py", label="215", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
