import streamlit as st
from inventory import display_inventory, check_inventory
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=87)

fr_text = """
Concentrant votre pouvoir de Seigneur Kaï sur la serrure, vous
essayez de vous en représenter le mécanisme. Peu à peu son
image se forme dans votre esprit et vous constatez qu'il est vieux
et usé, mais qu'il fonctionne toujours. L'intensité de votre
concentration commence à faiblir dangereusement lorsque vous
entendez enfin un faible déclic qui témoigne que vos efforts n'ont
pas été vains. Il est plus facile d'ôter la broche qui, lentement, se
dégage de ses attaches, puis tombe sur le sol. La porte de granité
tourne alors sur des gonds invisibles et la faible clarté qui baigne
le cimetière se répand dans le caveau. Le passage menant à
l'extérieur est envahi de ronces qui vous écorchent le visage et les
mains tandis que vous vous hissez au-dehors. Puis, soudain, au
moment où vous reparaissez enfin à l'air libre, un bruit vous fait
sursauter. Vous vous retournez et vous apercevez la tête d'un
cadavre décapité, une tête de mort aux chairs décomposées :
cette tête vous regarde et semble rire de toutes ses dents. Saisi
d'une panique aveugle, vous vous mettez aussitôt à courir de
toute la force de vos jambes et vous traversez l'effroyable
cimetière en direction de la porte sud de la capitale.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Rendez-vous """
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_61.py", label="61", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

