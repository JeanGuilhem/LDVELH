import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    is_good = called_cookies()
    if not is_good:
        st.stop()

st.session_state.current_page_number = 269
check_inventory(is_fighting=False,
                current_page_number=st.session_state.current_page_number)

fr_text = """
Le cadavre du vieux fou est étendu à vos pieds. Deux soldats
apparaissent alors dans l'encadrement de la porte cochère et
vous félicitent chaudement. Ils vous expliquent que le vieillard
était un dément échappé d'un asile et qu'ils essayaient depuis
deux jours de le rattraper. L'un des soldats vous offre 10 Pièces
d'Or en guise de récompense et vous propose de vous conduire à
la citadelle qui abrite le Palais du Roi.
"""

if st.session_state.last_page_number != st.session_state.current_page_number:
    st.session_state.purse += 10
    st.metric(label="Couronnes", value=st.session_state.purse, delta=10)


tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous acceptez son offre, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_314.py", label="314", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez ne compter que sur vous-même pour rejoindre la citadelle, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_7.py", label="7", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
