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
                current_page_number=96)

fr_text = """
Retenant votre souffle, vous resserrez votre prise et vous vous
préparez à frapper. La tension est insupportable. Les Gloks sont
si proches que vous pouvez sentir l'odeur immonde de leurs
corps malpropres. Vous les entendez pousser des jurons dans
leur étrange dialecte, puis quitter les abords de la grotte pour
grimper vers le sommet de la colline. Lorsque, enfin, vous êtes
sûr qu'ils se sont éloignés, vous respirez à nouveau et vous
essuyez la sueur qui ruisselle sur votre visage.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez inspecter la grotte plus avant, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_33.py", label="33", icon="📄")

    st.write_stream(
        stream_text(
            f"""Si vous préférez quitter les lieux et redescendre la colline, de peur que les
Gloks ne reviennent, rendez-vous au:"""
        )
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_248.py", label="248", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
