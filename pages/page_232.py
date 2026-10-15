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
                current_page_number=232)

fr_text = """
Leur chef, à l'allure patibulaire, s'approche de vous et vous
déclare ceci : « Ce que nous voulons ? C'est très simple, cher
monsieur : votre bourse ou votre vie ! »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez les combattre, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_180.py", label="180", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez tenter de vous enfuir, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_22.py", label="22", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
