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
                current_page_number=167)

fr_text = """
Vous avez parcouru environ deux kilomètres lorsque vous
apercevez deux jambes qui dépassent de derrière un gros rocher.
"""

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous voulez vous approcher pour voir de quoi il retourne, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_88.py", label="88", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez passer votre chemin et continuer droit devant, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_264.py", label="264", icon="📄")

    st.write_stream(
        stream_text(
            f"""Enfin, si vous maîtrisez la Discipline Kaï du Sixième Sens (et que vous désirez en faire usage), rendez-vous au:"""
        )
    )
    if has_kai("Le Sixième Sens"):
        st.page_link("pages/page_178.py", label="178", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("pages/page_178.py", label="178", icon="📄", disabled=True)

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
