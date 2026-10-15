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
                current_page_number=59)

fr_text = """
Scrutant l'obscurité, vous distinguez quelques marches taillées
grossièrement dans la terre et vous vous apercevez que cette
grotte est en fait l'entrée d'un tunnel. Vous descendez
prudemment les marches glissantes et vous découvrez au bas de
cet escalier de fortune une petite boîte en argent posée sur une
étagère.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez ouvrir la boîte, rendez-vous au"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_124.py", label="124", icon="📄")

    st.write_stream(
        stream_text(f"""Si
vous préférez ressortir et poursuivre votre chemin, rendez-vous
au""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_106.py", label="106", icon="📄")

    st.write_stream(
        stream_text(
            f"""Si vous choisissez enfin de vous enfoncer plus avant dans
le tunnel, rendez-vous au"""
        )
    )
    fi_2 = True
    if fi_2:
        st.page_link("pages/page_211.py", label="211", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
