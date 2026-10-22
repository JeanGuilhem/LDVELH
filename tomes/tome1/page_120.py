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
                current_page_number=120)

fr_text = """
Vous entendez les Gloks fous et sanguinaires tuer les autres
chevaux de la roulotte. Vous jetez alors un coup d'œil par-dessus
votre épaule : le Kraan s'est mis à tournoyer dans les airs. A-t-il
l'intention de vous attaquer ou s'intéresse-t-il à autre chose ?
L'ombre noire qui grandit bientôt tout autour de vous ne laisse
plus subsister le moindre doute : c'est bien après vous qu'il en a.
Le Kraan, en vérité, est même en train de fondre en piqué à une
vitesse fulgurante !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez attendre qu'il soit presque sur vous pour sauter au même moment de votre cheval, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_84.py", label="84", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez galoper vers les arbres pour vous mettre à couvert, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("tomes/tome1/page_171.py", label="171", icon="📄")

    st.write_stream(
        stream_text(
            f"""Si, enfin, il vous semble plus judicieux de baisser la tête et de prier le ciel de vous protéger, tandis que vous galoperez droit devant, rendez-vous au:"""
        )
    )
    fi_2 = True
    if fi_2:
        st.page_link("tomes/tome1/page_54.py", label="54", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
