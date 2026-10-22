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
                current_page_number=261)

fr_text = """
Ruisselant de sueur et le souffle court vous écartez les feuillages
sous lesquels vous vous êtes réfugié et vous apercevez un Kraan
qui vole au-dessus du chariot. Trois Gloks, au rictus diabolique,
sautent du Kraan et se laissent tomber par terre, devant les
chevaux effrayés. Ils s'avancent alors vers les enfants sans
défense en brandissant leurs lances.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez retourner vers le chariot pour porter secours aux enfants, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_208.py", label="208", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez vous enfoncer plus avant dans la forêt, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_264.py", label="264", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
