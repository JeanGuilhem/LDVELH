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
                current_page_number=239)

fr_text = """
Tandis que vous vous enfoncez dans la forêt, vous entendez
battre les ailes du Kraan qui passe en volant au-dessus des arbres
avant de disparaître en direction du nord. Vous chevauchez
pendant environ une heure, puis vous arrivez à une clairière. De
l'autre côté, face à vous, un sentier mène vers le sud.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez traverser la clairière pour prendre ce sentier orienté au
sud, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_34.py", label="34", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez rejoindre ce même
chemin en contournant la clairière, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_118.py", label="118", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
