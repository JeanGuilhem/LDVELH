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
                current_page_number=223)

fr_text = """
Après bien des efforts, vous parvenez à dégager le tronc de tous
les débris qui l'entourent. Vous attachez ensuite toutes vos
affaires en un paquet bien serré que vous coincez dans un creux
du tronc d'arbre, puis vous vous y installez vous-même à
califourchon. Le courant bientôt vous emporte et vous dérivez
lentement au fil de l'eau. Une vingtaine de minutes plus tard,
vous entendez des chevaux galoper au loin, sur la rive gauche.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez vous cacher derrière le tronc, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_75.py", label="75", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez signaler votre présence aux cavaliers qui s'approchent, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_175.py", label="175", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
