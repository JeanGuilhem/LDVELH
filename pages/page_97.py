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
                current_page_number=97)

fr_text = """
Un peu plus loin devant vous, une terrible bataille a lieu sur un
pont de pierre. Le fracas des armes, les cris des combattants et
les hennissements des chevaux retentissent en écho dans la forêt.
Une silhouette familière se dessine alors au beau milieu du pont,
là où les corps à corps sont les plus violents : vous reconnaissez
aussitôt le Prince Pellagayo, le fils du Roi. Il est en train de se
battre avec un énorme Gourgaz qui brandit une Hache Noire au-
dessus de sa tête couverte d'écaillés grisâtres. Or, un instant plus
tard, le Prince tombe de son cheval et s'écroule sur le pont,
atteint par une flèche qui lui a percé le flanc.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez vous porter au secours du Prince Pellagayo, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_255.py", label="255", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez vous enfuir dans la forêt, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_306.py", label="306", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
