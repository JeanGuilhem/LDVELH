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
                current_page_number=183)

fr_text = """
L'officier ordonne à ses hommes de s'arrêter et vous demande ce
que vous voulez. Vous lui expliquez qui vous êtes et vous lui
faites le récit de la destruction du Monastère. Consterné par la
nouvelle qu'il vient d'apprendre, il vous donne un cheval et vous
demande de le suivre auprès du Prince Pellagayo, le fils du Roi.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous acceptez sa proposition, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_97.py", label="97", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous refusez, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("tomes/tome1/page_200.py", label="200", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
