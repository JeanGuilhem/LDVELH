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
                current_page_number=320)

fr_text = """
Tandis que vous courez à terrain découvert en direction de la forêt, un Kraan fond sur vous et vous agrippe le bras. 
Avant même que vous ayez pu esquisser un geste pour vous défendre, il s'envole à nouveau et s'éloigne à tire-d'aile 
en lançant un cri à vous glacer le sang. Vous parvenez à pénétrer dans la forêt, mais vous avez perdu 2 points d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if st.session_state.last_page_number != st.session_state.current_page_number:
        st.session_state.endurance -= 2
        st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    st.write_stream(
        stream_text(
            f"""Rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_264.py", label="264", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
