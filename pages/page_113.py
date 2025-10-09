import streamlit as st
from inventory import display_inventory, check_inventory, add_to_inventory
from utils import stream_text, set_cookies, called_cookies, change_visiblity

if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=113)

fr_text = """
Vous avez marché pendant plus d'une demi-heure lorsque vous
apercevez des fleurs d'un rouge vif qui poussent sur un
monticule. Vous reconnaissez aussitôt cette plante : c'est du
Laumspur, une herbe rare très recherchée pour ses vertus
curatives. Vous cueillez alors une bonne poignée de cette herbe
que vous rangez dans votre Sac à Dos. Elle vous servira à
récupérer des points d'ENDURANCE lorsque vous en mangerez.
Chaque dose de Laumspur vous rendra 3 points d'ENDURANCE
et vous avez cueilli là l'équivalent de 2 doses. Vous refermez votre
Sac à Dos et vous poursuivez votre route.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    
    st.write("Vous pouvez ajouter les doses de Laumspur à votre inventaire :")

    if st.button(label="Dose de Laumspur", key="laumspur_1", disabled=st.session_state.visibility_1):
        st.session_state.visibility_1 = True # to hide next time the checkbox
        add_to_inventory(name="LAUMSPUR")
    if st.button(label="Dose de Laumspur", key="laumspur_2", disabled=st.session_state.visibility_2):
        st.session_state.visibility_2 = True
        add_to_inventory(name="LAUMSPUR")

    st.write_stream(
        stream_text(
            f"""Si vous souhaitez vous diriger vers le nord-est, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_347.py", label="347", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez aller à l'est, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_295.py", label="295", icon="📄")

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")