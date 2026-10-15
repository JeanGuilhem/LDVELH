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
                current_page_number=58)

fr_text = """
Vous vous lancez sur la route au pas de course en maintenant
une allure régulière. A l'ouest, l'armée des Maîtres des Ténèbres
ressemble à une immense tache d'encre noire qui se serait
répandue entre les montagnes. Vous courez depuis vingt minutes
environ lorsque vous apercevez à votre droite une meute de
Loups Maudits qui avancent en file indienne le long d'une
corniche.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez vous plaquer contre les rochers qui
bordent la route et attendre qu'ils soient passés, rendez-vous au
"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_286.py", label="286", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez continuer à courir en tirant votre épée
pour vous préparer à toute éventualité, rendez-vous au""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_160.py", label="160", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
