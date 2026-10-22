
import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, set_cookies, called_cookies, ls_death


if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    is_good = called_cookies()
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=309)

fr_text = """
Vous avez à peine fait dix pas lorsque le corbeau se met à
croasser pour avertir l'étranger de votre présence. Le personnage
fait alors volte-face et lance un cri perçant qui vous glace le sang
et vous noue l'estomac sous l'effet d'une peur panique. Car c'est
un Vordak que vous avez devant vous, un des plus cruels
lieutenants des Maîtres des Ténèbres. C'est également une
créature qui appartient au monde des morts vivants. En quelques
secondes, une horde de Gloks apparaissent à ses côtés et vous
attaquent. Vous vous défendez vaillamment, mais vous
succombez sous le nombre. Et bientôt, les doigts squelettiques du
Vordak se referment inexorablement sur votre gorge : c'est la
dernière sensation que vous emporterez de ce monde. Votre
mission s'achève ici en même temps que votre vie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    ls_death()

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
