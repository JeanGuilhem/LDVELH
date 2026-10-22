import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, change_endurance, remove_from_inventory
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=236)

fr_text = """
La Pierre Précieuse reste suspendue au-dessus de la bouche du
squelette en diffusant une lueur rouge vif.
Puis soudain, en une violente explosion, des flammes écarlates
jaillissent du sarcophage, détruisant complètement la Pierre de
Vordak. Vous êtes projeté contre le mur et assommé par le choc.
Lorsque vous reprenez connaissance, la chambre mortuaire est
complètement vide : le sarcophage et le squelette du roi ont tous
deux disparu. Quant à vous, les nouvelles ne sont pas bonnes :
vous avez, en effet, perdu 6 points d'ENDURANCE et votre total
d'HABILETÉ se trouve réduit de 1 point pour le reste de vos
jours. Vous vous relevez précautionneusement et vous vous
dirigez vers le tunnel en titubant.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if st.session_state.last_page_number != st.session_state.current_page_number:
        remove_from_inventory("PIERRE PRÉCIEUSE")  # la Pierre de Vordak est détruite
        st.session_state.hability -= 1
        change_endurance(-6)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-6)
    st.metric(label="Habileté", value=st.session_state.hability, delta=-1)

    st.write_stream(
        stream_text(f"""Rendez-vous au:""")
    )
    fi = True
    if fi:
        st.page_link("pages/page_104.py", label="104", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
