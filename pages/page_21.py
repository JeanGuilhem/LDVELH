import streamlit as st
from inventory import display_inventory, check_inventory
from utils import stream_text, set_cookies, called_cookies, table_des_hasards, ls_death

if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=21)

fr_text = """
Vous avez parcouru trois kilomètres à cheval parmi les arbres
touffus lorsque le sol devient soudain marécageux
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    if st.button(label="Utilisez la Table de Hasard pour obtenir 3 chiffres."):
        number1 = table_des_hasards()
        number2 = table_des_hasards()
        number3 = table_des_hasards()
        st.write_stream(stream_text(text=f"*Vous avez tiré une première fois le {number1}"))
        if number1 >= 5:
            st.write_stream(stream_text(f"""Vous parvenez à vous éloigner de ce bourbier et vous vous rendez au"""))
            st.page_link("pages/page_189.py", label="189", icon="📄")
        else:
            st.write_stream(stream_text(f"""Votre cheval s'est enfoncé jusqu'au ventre dans une
boue épaisse"""))
            st.write_stream(stream_text(text=f"*Vous avez tiré une deuxième fois le {number2}"))
            if number2 >= 7:
                st.write_stream(stream_text(f"""Vous réussissez tant bien que mal à vous hisser sur un sol plus
ferme et vous vous rendez au """))
                st.page_link("pages/page_189.py", label="189", icon="📄")
            else:
                st.write_stream(stream_text(f"""Vous vous enfoncez dans la boue
jusqu'aux aisselles. En poussant un ultime hennissement
désespéré, votre cheval, quant à lui, disparaît définitivement
dans la vase."""))
                st.write_stream(stream_text(text=f"*Vous avez tiré une dernière fois le {number3}"))
                if number3 != 9:
                    st.write_stream(stream_text(f"""Le marécage vous engloutit définitivement et votre
mission s'achève ici, en même temps que votre vie"""))
                    ls_death()
                else:
                    st.write_stream(stream_text(f"""Vous réussissez tant bien que mal à vous hisser sur un sol plus
                    ferme et vous vous rendez au """))
                st.page_link("pages/page_312.py", label="312", icon="📄")

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

