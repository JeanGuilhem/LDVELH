import streamlit as st
from inventory import display_inventory, check_inventory, add_to_inventory, end_page, has_kai
from utils import stream_text, set_cookies, called_cookies, handle_repas, ls_death


if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=130)

fr_text = """
Vous parvenez bientôt à une petite clairière. En son centre, vous
trouvez un banc taillé dans le tronc d'un arbre.
Vous avez faim, et il vous faut prendre un Repas, sinon, vous
perdrez 3 points d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    handle_repas()

    st.write_stream(
        stream_text(
            f"""Lorsque vous avez fini de manger, vous pourrez quitter la clairière par le sud en vous rendant au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_28.py", label="28", icon="📄")

    st.write_stream(
        stream_text(f"""Mais si vous préférez emprunter le sentier plus étroit qui mène vers l'est en s'enfonçant dans la forêt, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_201.py", label="201", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
