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
                current_page_number=85)

fr_text = """
Le chemin est large et mène droit à un enchevêtrement de
broussailles. Les arbres sont très hauts à cet endroit, et il y règne
un silence inhabituel. Vous parcourez plus de deux kilomètres et
vous entendez soudain un battement d'ailes au-dessus de vous.
En levant les yeux, vous apercevez alors avec un frémissement
d'horreur la silhouette noire et sinistre d'un Kraan qui fond sur
vous. 
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f""" Si vous décidez de dégainer votre arme pour le combattre,
rendez-vous au """
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_229.py", label="229", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez essayer de vous enfuir en
courant vers le sud pour vous enfoncer plus profondément dans
la forêt, rendez-vous au""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("tomes/tome1/page_99.py", label="99", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
