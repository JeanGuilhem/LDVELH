import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, set_cookies, called_cookies, ls_death



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=271)

fr_text = """
Vous vous sentez très faible. Le venin du serpent circule à
présent dans votre sang et vos muscles se raidissent, puis se
détendent. Vos jambes bientôt se dérobent et vous vous enfoncez
alors dans la vase pestilentielle du marécage qui vous engloutit
en quelques instants. Votre vie vient de s'achever.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    ls_death()

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
