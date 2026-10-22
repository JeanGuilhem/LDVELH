import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, spend_gold, show_illustrations
from utils import stream_text, set_cookies, called_cookies


if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=12)

fr_text = """
Le garde du corps vous observe d'un regard soupçonneux puis
vous claque la porte au nez. Vous entendez alors des voix à
l'intérieur de la roulotte, puis, soudain, la porte s'ouvre à
nouveau et un marchand à l'allure prospère apparaît devant
vous. Il exige 10 Couronnes pour prix de votre transport.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text("Si vous avez ces 10 Couronnes et que vous désirez les lui donner, rendez-vous au :")
    )
    if st.button("Payer 10 Couronnes (262)", disabled=st.session_state.purse < 10):
        if spend_gold(10):
            st.switch_page("tomes/tome1/page_262.py")
    if st.session_state.purse < 10:
        st.caption("Vous ne possédez pas la somme requise.")

    st.write_stream(
        stream_text("Si vous n'avez pas cette somme, ou si vous ne souhaitez pas la lui payer, rendez-vous au :")
    )
    st.page_link("tomes/tome1/page_247.py", label="247", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
