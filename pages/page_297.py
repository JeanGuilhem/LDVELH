
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
                current_page_number=297)

fr_text = """
Mettant en pratique vos talents de chasseur, vous vous frayez
lentement un passage à travers l'épaisse végétation sans vous
faire repérer. Moins d'une minute plus tard, vous vous trouvez
derrière le poteau auquel le soldat est attaché. Le bois a été
allumé à ses pieds et un nuage de fumée commence déjà à
envelopper le malheureux. Vous empoignez alors votre Hache et
vous vous ruez en avant, profitant de la fumée pour vous
dissimuler aux regards. D'un seul coup de Hache, vous coupez la
corde qui retient le soldat prisonnier et vous l'emmenez aussitôt
à l'abri de la forêt. Tandis que vous avancez parmi les arbres, les
Gloks se mettent à pousser des cris : ils viennent de s'apercevoir
que leur victime s'est littéralement volatilisée dans un nuage de
fumée.
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
        st.page_link("pages/page_117.py", label="117", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
