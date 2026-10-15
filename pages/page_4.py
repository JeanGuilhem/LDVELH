import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai
from utils import stream_text, set_cookies, called_cookies
from text import fr_unkown_kai


if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=4)

fr_text = """
C'est un petit canoë à une place, en très mauvais état. Des pièces
de bois disjointes laissent apparaître des trous en plusieurs
endroits de la coque et il vous faut les boucher à la hâte avec de
l'argile. Vous videz ensuite l'embarcation de son eau et il vous
semble alors qu'elle est en état de flotter. Vous rangez votre
équipement à l'avant du canoë, puis vous descendez le cours de
la rivière en pagayant à l'aide d'un débris de bois ramassé à la
surface de l'eau. Un instant plus tard, vous entendez des chevaux
galoper dans votre direction, le long de la rive gauche.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous
souhaitez vous cacher au fond du canoë, rendez-vous au"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_75.py", label="75", icon="📄")

    st.write_stream(
        stream_text(f"""Si
vous préférez au contraire attirer l'attention des cavaliers,
rendez-vous au""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_175.py", label="175", icon="📄")

    st.write_stream(
        stream_text(
            f"""Si vous maîtrisez la Discipline Kaï du
Sixième Sens, rendez-vous au"""
        )
    )
    fi_2 = True
    if fi_2:
        if has_kai("Le Sixième Sens"):
            st.page_link("pages/page_218.py", label="218", icon="📄")
        else:
            st.write_stream(
                    stream_text(
                            fr_unkown_kai
                    )
            )
        st.page_link("pages/page_218.py", label="218", icon="📄", disabled=True)


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
