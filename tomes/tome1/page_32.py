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
                current_page_number=32)

fr_text = """
Vous avez parcouru environ cinq kilomètres à cheval lorsque
vous apercevez à quelque distance la silhouette caractéristique de
cinq grands Loups Maudits. Des Gloks les chevauchent et ils
semblent se diriger vers une prairie située au bout du chemin.
Soudain, l'un des Gloks s'écarte de ses compagnons et revient sur
ses pas, lançant sa monture en direction de l'endroit où vous
vous trouvez.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez vous cacher dans les sous-bois et
le laisser passer, rendez-vous au"""
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_176.py", label="176", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez le
combattre, rendez-vous au""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("tomes/tome1/page_340.py", label="340", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
