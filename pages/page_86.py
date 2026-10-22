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
                current_page_number=86)

fr_text = """
Vous atteignez bientôt un nouveau croisement.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f""" Si vous voulez
aller vers l'est, rendez-vous au """
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_6.py", label="6", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez prendre la
direction du nord, rendez-vous au""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_35.py", label="35", icon="📄")

    st.write_stream(
        stream_text(
            f"""Si vous estimez plus
judicieux d'aller vers le sud, rendez-vous au"""
        )
    )
    fi_2 = True
    if fi_2:
        st.page_link("pages/page_167.py", label="167", icon="📄")

    st.write_stream(
            stream_text(
                f"""Si enfin vous
décidez plutôt de tourner vers l'ouest, rendez-vous au"""
            )
        )
    fi_3 = True
    if fi_3:
        st.page_link("pages/page_42.py", label="42", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
