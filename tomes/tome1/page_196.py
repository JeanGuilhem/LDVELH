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
                current_page_number=196)

fr_text = """
Vous suivez l'homme dans une petite bibliothèque contiguë. Il
pousse alors l'un des nombreux livres alignés sur les étagères et
vous entendez un déclic. Aussitôt, tout un pan d'étagères glisse
sur lui-même, découvrant un passage secret.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez suivre cet homme dans le passage, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_332.py", label="332", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous ne voulez pas pénétrer dans ce sombre couloir, vous quittez les lieux et vous retournez dans la rue en vous rendant au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("tomes/tome1/page_144.py", label="144", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
