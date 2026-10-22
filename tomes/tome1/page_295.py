
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
                current_page_number=295)

fr_text = """
Vous avez repris votre marche depuis un quart d'heure environ
lorsque une flèche noire siffle soudain à vos oreilles et vient se
planter dans un arbre juste devant vous. Instinctivement, vous
vous baissez en dégainant votre arme.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez rester où vous êtes pour essayer de repérer celui qui vous a tiré dessus, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_185.py", label="185", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez courir vous réfugier dans les épaisses broussailles qui vous entourent, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("tomes/tome1/page_92.py", label="92", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
