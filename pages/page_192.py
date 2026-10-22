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
                current_page_number=192)

fr_text = """
Vous distinguez la gueule hérissée de dents pointues d'un Loup Maudit et vous entendez les cris monstrueux des Gloks. Deux d'entre eux viennent droit sur vous, mais votre cheval vous sauve d'une mort certaine en sautant sur les Loups Maudits qu'il projette à terre à grands coups de sabot. Vous frappez un Glok à toute volée et votre arme lui ouvre la tête. Alors, soudain, comme par miracle, vous vous retrouvez galopant sur la grand-route : vous avez réussi à traverser la meute hurlante qui se trouve à présent derrière vous. Vous sentez, cependant, une présence menaçante au-dessus de votre tête : c'est celle d'un Kraan qui vient de prendre son envol.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez quitter la grand-route pour vous réfugier à l'abri des arbres de la forêt, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_171.py", label="171", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez continuer tout droit en galopant à bride abattue sans vous occuper du Kraan, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_120.py", label="120", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
