import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, pickup_button, pickup_gold
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=184)


fr_text = """
La roulotte a échappé à tout contrôle et cahote dangereusement
sur le bas-côté de la route, parmi les pierres et les nids-de-poule.
Vous parvenez cependant, au prix de bien des efforts, à ramener
sur la chaussée les chevaux saisis de panique et à arrêter
l'attelage. En fouillant rapidement le véhicule, vous découvrez 40
Pièces d'Or, une Epée et une quantité de nourriture équivalant à
4 Repas. Si vous souhaitez conserver l'une ou l'autre de ces
trouvailles (ou toutes ensemble), inscrivez-les sur votre Feuille
d'Aventure. Les épreuves que vous avez subies vous ont épuisé,
et il vous faut prendre un Repas. Vous plongerez ensuite dans un
sommeil profond.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Vous pouvez ajouter les objets suivants à votre inventaire :"))

    # Le Repas obligatoire est pris sur la nourriture trouvée ici (4 Repas), sauf avec la Chasse
    if has_kai("La Chasse"):
        st.success("*Grâce à votre Discipline Kaï de la Chasse, vous trouvez votre nourriture par vous-même.*")
        meals_left = 4
    else:
        st.info("Vous prenez votre Repas sur la nourriture trouvée dans la roulotte.")
        meals_left = 3

    pickup_gold(40)
    pickup_button("ÉPÉE", key="sword", label="Prendre l'Épée")
    for meal in range(1, meals_left + 1):
        pickup_button("REPAS", key=f"meal_{meal}", label="Prendre un Repas")

    st.write_stream(
        stream_text(f"""Rendez-vous au:""")
    )
    fi = True
    if fi:
        st.page_link("pages/page_64.py", label="64", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
