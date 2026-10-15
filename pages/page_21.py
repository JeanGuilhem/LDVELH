import streamlit as st
from inventory import display_inventory, check_inventory, end_page
from utils import stream_text, called_cookies, hazard_roll, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=21)

fr_text = """
Vous avez parcouru trois kilomètres à cheval parmi les arbres
touffus lorsque le sol devient soudain marécageux.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    first = hazard_roll(key="first")
    if first is not None and first >= 5:
        st.write_stream(stream_text("Vous parvenez à vous éloigner de ce bourbier."))
        st.page_link("pages/page_189.py", label="189", icon="📄")
    elif first is not None:
        st.write_stream(
            stream_text(
                "Votre cheval s'est enfoncé jusqu'au ventre dans une boue épaisse. "
                "Utilisez à nouveau la Table de Hasard pour tirer un autre chiffre."
            )
        )
        second = hazard_roll(key="second", label="Tirez un autre chiffre sur la Table de Hasard.")
        if second is not None and second > 7:
            st.write_stream(
                stream_text(
                    "Vous réussissez tant bien que mal à vous hisser sur un sol plus ferme."
                )
            )
            st.page_link("pages/page_189.py", label="189", icon="📄")
        elif second is not None:
            st.write_stream(
                stream_text(
                    "Vous vous enfoncez dans la boue jusqu'aux aisselles. En poussant un ultime "
                    "hennissement désespéré, votre cheval, quant à lui, disparaît définitivement "
                    "dans la vase. Voici votre dernière chance ! Tirez un autre chiffre à l'aide "
                    "de la Table de Hasard."
                )
            )
            third = hazard_roll(key="third", label="Tentez votre dernière chance sur la Table de Hasard.")
            if third == 9:
                st.page_link("pages/page_312.py", label="312", icon="📄")
            elif third is not None:
                st.write_stream(
                    stream_text(
                        "Le marécage vous engloutit définitivement et votre mission s'achève ici, "
                        "en même temps que votre vie."
                    )
                )
                ls_death()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
