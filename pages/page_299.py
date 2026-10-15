import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=299)

fr_text = """
Vous vous apercevez bientôt que vous venez d'aborder une région marécageuse. 
Continuer dans cette direction serait dangereux et ralentirait votre avance.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez poursuivre malgré tout, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_227.py", label="227", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez changer de direction et retrouver un terrain plus ferme, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_95.py", label="95", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
