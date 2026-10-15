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
                current_page_number=175)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
De la main, vous faites signe aux cavaliers en qui vous
reconnaissez des Gardes-Frontières de l'armée du Roi. Ils font
partie du régiment chargé de surveiller les frontières occidentales
du Royaume, souvent menacées. Mais le soulagement que vous
éprouvez à rencontrer des alliés est de courte durée, car vous
vous apercevez bientôt que ces soldats sont, en fait, poursuivis
par des Gloks hurlants qui chevauchent des Loups Maudits. Des
flèches noires tombent en pluie tout autour des Gardes-
Frontières tandis que leurs terribles poursuivants gagnent du
terrain.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous voulez essayer de vous cacher là où vous êtes, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_41.py", label="41", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez traverser la rivière à la nage pour vous réfugier sur l'autre berge, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_116.py", label="116", icon="📄")

    st.write_stream(
        stream_text(
            f"""Enfin, si vous maîtrisez la Discipline Kaï du Camouflage, rendez-vous au:"""
        )
    )
    if has_kai("Le Camouflage"):
        st.page_link("pages/page_182.py", label="182", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("pages/page_182.py", label="182", icon="📄", disabled=True)


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
