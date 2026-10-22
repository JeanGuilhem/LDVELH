import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, set_cookies, called_cookies


if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    is_good = called_cookies()
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=303)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
La forêt en cet endroit est clairsemée et le terrain vallonné. Aussi
n'avez-vous guère de possibilité de vous mettre à couvert en cas
d'attaque aérienne. Vous avancez donc aussi vite que possible
d'arbre en arbre pour éviter d'être repéré par des Kraans mais
entendez bientôt derrière grognements caractéristiques: ce sont des
Loups Maudits qui galopent à quelque distance.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous maîtrisez la Discipline Kaï du Camouflage, rendez-vous au:"""
        )
    )
    if has_kai("Le Camouflage"):
        st.page_link("pages/page_237.py", label="237", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("pages/page_237.py", label="237", icon="📄", disabled=True)

    st.write_stream(
        stream_text(f"""Sinon, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_72.py", label="72", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
