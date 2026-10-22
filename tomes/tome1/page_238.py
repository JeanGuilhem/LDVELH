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
                current_page_number=238)

fr_text = """
Le sentier contourne plusieurs tertres et collines aux flancs
boisés, puis aboutit enfin à une petite cabane en rondins
incendiée. Il semble qu'elle ait brûlé tout récemment car les
cendres sont encore chaudes, et il s'en élève un filet de fumée. Il
se peut que cet endroit soit dangereux.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez repartir par le sentier orienté au sud, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_42.py", label="42", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez emprunter le chemin qui mène vers le nord, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("tomes/tome1/page_68.py", label="68", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
