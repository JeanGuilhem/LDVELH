import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai
from utils import stream_text, set_cookies, called_cookies


if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    is_good = called_cookies()
    if not is_good:
        st.stop()

current_page_number = 334
check_inventory(is_fighting=False,
                current_page_number=current_page_number)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Le cours d'eau prend sa source dans le flanc rocheux d'une
colline et, en levant les yeux, vous apercevez sur un chemin qui
longe la pente escarpée quatre soldats et leur officier. Ils portent
des uniformes de l'Armée Royale.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez vous approcher d'eux, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_162.py", label="162", icon="📄")

    st.write_stream(
        stream_text(
            f"""Si vous maîtrisez la Discipline Kaï du Camouflage, vous pouvez la mettre en pratique
            et vous cacher en attendant que les soldats soient passés. Rendez-vous pour cela au:"""
        )
    )
    if has_kai("Le Camouflage"):
        st.page_link("pages/page_73.py", label="73", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("pages/page_73.py", label="73", icon="📄", disabled=True)

    st.write_stream(
        stream_text(
            f"""Si, enfin, vous maîtrisez la Discipline Kaï du Sixième Sens et que vous souhaitez en faire
            usage, rendez-vous au:"""
        )
    )
    if has_kai("Le Sixième Sens"):
        st.page_link("pages/page_48.py", label="48", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("pages/page_48.py", label="48", icon="📄", disabled=True)


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
