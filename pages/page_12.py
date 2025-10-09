import streamlit as st
from inventory import display_inventory, check_inventory
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
        stream_text(
            f"""Si vous
avez ces 10 Couronnes et que vous désirez les lui donner, rendez-
vous au"""
        )
    )
    if st.session_state.purse >= 10:
        fi = True
        if fi:
            st.page_link("pages/page_262.py", label="262", icon="📄")
    else:
        st.write(stream_text("Vous ne possedez pas la somme requise."))
        fi = True
        if fi:
            st.page_link("pages/page_85.py", label="85", icon="📄",disabled=True)

    st.write_stream(
        stream_text(f"""Si vous n'avez pas cette somme, ou si vous ne
souhaitez pas la lui payer, rendez-vous au""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_247.py", label="247", icon="📄")

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

