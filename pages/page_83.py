import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, show_illustrations
from text import fr_unkown_kai
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=83)

fr_text = """
Vous avez couru pendant presque deux kilomètres lorsque trois
soldats surgissent de sous un petit pont. Ils vous ordonnent de
vous arrêter et de déposer à terre vos armes et tout votre
équipement. Leurs uniformes sont tachés de sang et ils ont
négligé de se raser. Leur chef porte une tunique de la garnison de
Toran.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f""" Si vous décidez de leur obéir, rendez-vous au"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_205.py", label="205", icon="📄")

    st.write_stream(
        stream_text(f"""Si
vous préférez vous préparer à les combattre, rendez-vous au""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_180.py", label="180", icon="📄")

    st.write_stream(
        stream_text(
            f"""Si vous souhaitez leur demander ce qu'ils veulent, rendezvous au"""
        )
    )
    fi_2 = True
    if fi_2:
        st.page_link("pages/page_232.py", label="232", icon="📄")

    st.write_stream(
        stream_text(
            f"""Enfin, si vous maîtrisez la Discipline Kaï du
Sixième Sens, rendez-vous au"""
        )
    )
    fi_3 = True
    if fi_3:
        if has_kai("Le Sixième Sens"):
            st.page_link("pages/page_45.py", label="45", icon="📄")
        else:
            st.write_stream(
                stream_text(
                    fr_unkown_kai
                )
            )
            st.page_link("pages/page_45.py", label="45", icon="📄", disabled=True)

    show_illustrations()



with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
