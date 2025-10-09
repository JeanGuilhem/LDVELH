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
                current_page_number=119)

fr_text = """
Les Brosses à Potence déchirent votre cape et vous écorchent
bras et jambes tandis que vous vous frayez un chemin dans leur
enchevêtrement d'épines. Un quart d'heure plus tard, vous sortez
enfin des buissons et vous poursuivez votre route d'un pas
chancelant, mais parmi les arbres cette fois. Les plaies
occasionnées par les Brosses à Potence vous coûtent 2 points
d'ENDURANCE. Alors que vous continuez d'avancer, vous vous sentez pris de vertiges et vos
paupières vous semblent lourdes. Bientôt, vous arrivez au bord
d'une pente escarpée et couverte d'arbres.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    
    # Perte d'ENDURANCE
    if st.session_state.last_page_number != st.session_state.current_page_number:
        st.session_state.endurance -= 2
        
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)
    
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez vous laisser glisser le long de cette pente en prenant bien garde à ne pas tomber, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_226.py", label="226", icon="📄")

    st.write_stream(
        stream_text(
            f"""Si, en revanche, vous ne voulez pas prendre le risque de descendre la pente dans l'état de somnolence où vous êtes, vous marcherez le long du bord en vous rendant au:"""
        )
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_38.py", label="38", icon="📄")
    
    st.session_state.last_page_number =  st.session_state.current_page_number

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

