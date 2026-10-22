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
                current_page_number=316)

fr_text = """
Dans votre hâte de fuir l'ennemi, vous vous prenez le pied dans
une racine et vous tombez tête la première en soulevant un nuage
de poussière et de feuilles. Vous atterrissez dans les broussailles,
au pied de la colline et vous vous relevez aussitôt pour courir
vous réfugier dans la forêt après avoir ramassé votre Arme. Le
Kraan qui tournoyait dans le ciel a disparu, mais vous apercevez,
au sommet de la colline, la silhouette de deux Gloks auxquels il
vous faut échapper. Vous essuyez la poussière de votre visage et
vous vous apercevez alors que vous avez une grosse bosse sur le
front qui vous fait grimacer de douleur lorsque vous passez la
main dessus. Sans perdre une minute, vous prenez vos jambes à
votre cou et vous disparaissez dans l'épaisseur de la forêt.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_331.py", label="331", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
