
import streamlit as st
from inventory import display_inventory, check_inventory, add_to_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, set_cookies, called_cookies, handle_repas, table_des_hasards, ls_death


if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

st.session_state.current_page_number = 349
check_inventory(is_fighting=False,
                current_page_number=st.session_state.current_page_number)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
C'est un jeune homme aux cheveux blonds et au regard pénétrant. Son visage est marqué par la fatigue et souillé par la poussière des combats. Ses amples vêtements bleu ciel, déchirés par endroits, montrent à l'évidence que le magicien a passé de longs jours dans la forêt. Il vous serre la main et s'incline. « Soyez assuré de mon éternelle gratitude, Seigneur Kaï, dit-il, mes pouvoirs magiques étaient presque épuisés et, si vous n'étiez pas venu à mon secours, je crois bien que j'aurais fini mes jours au bout de la lance d'un Glok. » Il semble affaibli et ses jambes ont du mal à le porter. Vous le prenez alors par le bras et vous le faites asseoir sur une des colonnes renversées du Temple, puis vous écoutez ce qu'il a à vous dire. «Je m'appelle Banedon, poursuit-il, je suis compagnon de la Confrérie de l'Étoile de Cristal, c'est-à-dire la Guilde des Magiciens de Toran. Mon maître m'a envoyé à votre monastère pour porter ce message urgent. » En prononçant ces mots, il sort d'une poche de ses vêtements une enveloppe de vélin qu'il vous tend. « Comme vous pouvez le voir, reprend-il, j'ai ouvert la lettre et j'en ai lu le contenu. Lorsque la guerre a commencé, je me trouvais sur la grand-route, cheminant avec deux compagnons de voyage. Des Kraans nous ont attaqués et nous nous sommes enfuis dans la forêt, mais nous n'avons pas pu nous retrouver par la suite. » La lettre avertit les Seigneurs Kaï que les Maîtres des Ténèbres ont rassemblé une immense armée au-delà des monts Durncrag. Les Maîtres de la Guilde conjurent les Seigneurs Kaï d'annuler les cérémonies organisées pour la fête de Fehmarn et de se préparer à la guerre. « Hélas ! je crois bien que nous avons été trahis, dit Banedon en penchant la tête d'un air consterné. L'un des compagnons de mon ordre, en effet, un frère du nom de Vonotar, s'est initié aux mystères interdits de la Magie Noire. Il y a dix jours, il a renié la Confrérie et tué l'un de nos Anciens. Depuis, il a disparu et il semble bien qu'il se soit mis au service des Maîtres des Ténèbres. » Vous révélez alors à Banedon ce qu'il est advenu du monastère et vous l'informez de la mission que vous vous êtes fixée auprès du Roi. Lorsque vous avez terminé votre récit, il ôte de son cou une Chaîne d'Or et vous la donne. Une petite Étoile de Cristal est attachée à la chaîne. « C'est le symbole de ma Confrérie, explique le magicien, et, en ces heures sombres, nous sommes frères tous deux. Aussi, prenez ce talisman qui vous portera bonheur. Puisse-t-il vous protéger au long de votre route ! » Vous le remerciez, vous passez la Chaîne autour de votre cou et vous glissez l'Étoile de Cristal dans votre chemise, tout contre votre poitrine (n'oubliez pas d'inscrire ce pendentif à l'Etoile de Cristal dans la case Objets Spéciaux de votre Feuille d'Aventure). Banedon ensuite vous dit adieu.
« Il nous faut quitter ces lieux, assure-t-il, de peur que les Gloks ne reviennent accompagnés de renforts. Ces répugnantes créatures auraient alors raison de nous. Je dois à présent retourner à la Guilde. Au revoir, mon frère, que la chance des Dieux vous accompagne. »
"""

if "visibility_crystal_star_chain" not in st.session_state:
    st.session_state.visibility_crystal_star_chain = False

if st.session_state.last_page_number != st.session_state.current_page_number:
    if not st.session_state.visibility_crystal_star_chain:
        add_to_inventory(name="Pendentif à l'Etoile de Cristal")
        st.session_state.visibility_crystal_star_chain = True


tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_293.py", label="293", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
