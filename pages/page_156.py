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
                current_page_number=156)

fr_text = """
Des flèches noires se fichent dans la boue tout autour de vous.
D'autres Gloks ont fait leur apparition sur la berge escarpée de la
rivière et vous tirent dessus. De ce côté du cours d'eau, il n'y a
pas d'arbres pour vous mettre à l'abri.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez plonger dans l'eau de la rivière et nager au fil du courant, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_294.py", label="294", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez traverser le cours d'eau à la nage pour aller vous mettre à couvert des arbres, sur la rive opposée, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_245.py", label="245", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
