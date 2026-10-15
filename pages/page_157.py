
import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    is_good = called_cookies()
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=157)

fr_text = """
La forêt s'éclaircit et vous apercevez bientôt une route un peu plus loin. Une véritable foule occupe toute la largeur de la chaussée et des hommes et des femmes tirent des carrioles remplies d'objets, de meubles ou de vêtements. Ce sont des réfugiés qui fuient le nord du royaume.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez vous joindre à ces réfugiés qui pourront peut-être vous donner des informations sur ce qui se passe dans le nord, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_30.py", label="30", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez poursuivre votre route vers le sud, mais en restant à l'abri des arbres, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_167.py", label="167", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
