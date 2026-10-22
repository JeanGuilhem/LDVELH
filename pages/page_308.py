
import streamlit as st
from inventory import display_inventory, check_inventory, add_to_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, set_cookies, called_cookies, ls_death, handle_repas, table_des_hasards


if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=308)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
La porte de l'écurie est ouverte et vous entendez à l'intérieur la
respiration d'un cheval. Or, soudain, le cheval sent votre
présence et, pris de peur, se précipite au-dehors en vous
projetant passage.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if st.session_state.last_page_number != st.session_state.current_page_number:
        st.session_state.endurance -= 1
        st.metric(label="Endurance", value=st.session_state.endurance, delta=-1)

    st.write_stream(
        stream_text(
            f"""Si vous maîtrisez la Discipline Kaï de la Communication Animale et que vous souhaitez en faire usage, rendez-vous au:"""
        )
    )
    if has_kai("La Communication Animale"):
        st.page_link("pages/page_122.py", label="122", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("pages/page_122.py", label="122", icon="📄", disabled=True)

    st.write_stream(
        stream_text(f"""Sinon, vous vous lancerez à la poursuite du cheval en vous rendant au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_233.py", label="233", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
