import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, pickup_button, show_illustrations
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=15)

fr_text = """
Vous longez un long tunnel sombre formé par des branches
d'arbres qui s'entrecroisent au-dessus de votre tête et vous
arrivez enfin dans une vaste clairière. En son centre se dresse un
socle de pierre sur lequel est posée une épée, rangée dans un
fourreau de cuir noir. Un mot manuscrit est attaché à la garde de
l'épée, mais il est écrit dans une langue qui vous est étrangère.
Vous pouvez prendre cette épée si vous le désirez. Trois chemins
permettent de quitter la clairière
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("ÉPÉE", key="sword", label="Prendre l'épée")

    st.write_stream(
        stream_text(
            f"""Si vous voulez aller à l'est,
rendez-vous au"""
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_207.py", label="207", icon="📄")

    st.write_stream(
        stream_text(f"""A l'ouest, rendez-vous au""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("tomes/tome1/page_201.py", label="201", icon="📄")

    st.write_stream(
        stream_text(
            f"""Au sud,
rendez-vous au"""
        )
    )
    fi_2 = True
    if fi_2:
        st.page_link("tomes/tome1/page_35.py", label="35", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
