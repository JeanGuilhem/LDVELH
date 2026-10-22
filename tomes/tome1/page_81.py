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
                current_page_number=81)

fr_text = """
Une heure plus tard environ, les Kraans et leurs terribles
cavaliers disparaissent en direction de l'ouest. Les réfugiés,
tremblants de peur, sortent alors de la forêt, et vous entendez au
même moment des chevaux au galop s'approcher de l'endroit où
vous êtes. Ce sont des soldats de la cavalerie royale qui portent
l'uniforme blanc des armées de Sa Majesté.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez leur
faire signe, rendez-vous au"""
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_183.py", label="183", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez poursuivre
votre chemin vers le sud en longeant la lisière de la forêt, rendezvous au""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("tomes/tome1/page_200.py", label="200", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
