import streamlit as st

st.set_page_config(page_title="Accueil", layout="wide")

st.sidebar.success("Select Any Page from here")

st.markdown("""
    <style>

    [data-testid="stHeader"]{
     background-color:rgba(255,255,255,0);
     }

    #hotel-luxury{
    font-size:60px;
    margin-top:150px;
    margin-left:300px;
    font-family:serif;
    margin-bottom:400px;
    }


    [data-testid="stAppViewContainer"] {
        background-image:  linear-gradient(155deg, rgba(12, 13, 20, 0.300) 0%, rgba(2, 3, 3, 0.700) 100%),url("https://wallpapercave.com/wp/wp12814430.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        height: 100%;

    }
    [data-testid="stAppDeployButton"]{
    visibility:hidden;}


    [data-testid="stSidebar"]{
    background-color:rgba(3,3,0,0.7);}
    [data-testid="stSidebarHeader"]{
    background-image: url(https://media.istockphoto.com/id/1092200002/vector/luxury-hotel-logo-vector-design-on-black-background.jpg?s=612x612&w=0&k=20&c=GiriWYtD7uai5bf6Ac23IVCE2NKpSc5X3CGf6cUq47U=);
    background-size: cover;
    background-repeat: no-repeat; 
    height:150px;
    border-radius:15px;
    margin-bottom:70px;
    }
    h1, h2, h3, h4, h5 {
    color: white !important;
}
#avis-des-clients{
margin-top:300px;
}
   [data-testid="stToolbar"]{
    background-color:transparent;
}
p, label, span, li {
    color: #F5F5DC !important;
    font-size: 16px;
}
#les-caracteristiques-de-notre-hotel{
    margin-bottom:100px;
    font-family:serif;

}
[data-testid="stHorizontalBlock"]{
    margin-bottom:300px;
}
    </style>
    """

            , unsafe_allow_html=True)

main_container = st.container()
with main_container:
    st.title("Hotel Luxury\n\n\n\n\n")

st.title("Les caractéristiques de Notre hôtel:")
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://img.icons8.com/ios-filled/50/ffffff/swimming-pool.png")
    st.subheader("Piscine")
    st.write("Détendez-vous dans notre piscine luxueuse.")
    st.caption("Ouverte tous les jours de 8h à 22h, chauffée en hiver.")

with col2:
    st.image("https://img.icons8.com/ios/50/ffffff/spa.png")
    st.subheader("Spa & Bien-être")
    st.write("Reposez votre esprit et votre corps.")
    st.caption("Massages relaxants et soins exclusifs pour tous nos clients.")

with col3:
    st.image("https://img.icons8.com/ios/50/ffffff/restaurant.png")
    st.subheader("Restauration")
    st.write("Profitez d'expériences culinaires raffinées.")
    st.caption("Menus variés avec options végétariennes et desserts maison.")


# Section Actualités / Promotions
st.header("Nos Offres: ")

st.markdown(
    """
    <div style="
        background: rgba(0, 0, 0, 0.3);  /* fond semi-transparent noir pour rester dans le thème */
        padding: 20px;
        border-radius: 15px;
        margin-top: 40px;
        margin-bottom: 100px;
    ">
        <h3>🔥 Offres spéciale ce mois !</h3>
        <p>Profitez de -20% sur les suites ce mois-ci !</p>
        <p>Accès gratuit au spa pour toute réservation de plus de 3 nuits!</p>
        <p>Réservez votre séjour avec un dîner offert pour deux personnes.</p>
        </div>
    """,
    unsafe_allow_html=True
)

st.divider()

footer_container = st.container()
with footer_container:
    # tetstimonials section

    st.subheader("Avis des clients")
    st.write("Voici ce que nos clients disent de nous:")

    testimonial_1, testimonial_2, testimonial_3 = st.columns(3)

    with testimonial_1:
        st.write('"Expérience incroyable!"')
        st.caption("- Alice")

    with testimonial_2:
        st.write('"Personnel très accueillant."')
        st.caption("- Karim")

    with testimonial_3:
        st.write('"Séjour luxueux et inoubliable."')
        st.caption("- Leila")
    st.markdown("---")
    # ---------------- FAQ Section ----------------
    st.title("Foire aux Questions (FAQ)")

    with st.expander("Quels sont les horaires d'ouverture de l'hôtel ?"):
        st.write("Notre hôtel est ouvert 24h/24 et 7j/7 pour vous accueillir.")

    with st.expander("Est-ce que l'hôtel propose un service de navette ?"):
        st.write("Oui, nous proposons un service de navette aéroport sur réservation.")

    with st.expander("Les animaux de compagnie sont-ils autorisés ?"):
        st.write("Oui, les animaux de compagnie sont acceptés sous certaines conditions.")

    with st.expander("Proposez-vous des formules tout compris ?"):
        st.write("Oui, nous avons plusieurs formules adaptées à vos besoins et préférences.")

    st.divider()
    st.markdown("""<div style="
                                width:100%;
                                height:2px;
                                background-color:transparent;
                                margin-top:300px;"></div>""", unsafe_allow_html=True)
    st.write("Contactez-nous:")
    contact, facebook, phone, email = st.columns([2, 2, 2, 2])
    with contact:
        st.image("https://img.icons8.com/ios/50/ffffff/instagram.png")
        st.subheader("Instagram")
    with facebook:
        st.image("https://img.icons8.com/ios/50/ffffff/facebook.png")
        st.subheader("Facebook")

    with phone:
        st.image("https://img.icons8.com/ios/50/ffffff/phone.png")
        st.subheader("+212 05 99 99 99 99")

    with email:
        st.image("https://img.icons8.com/ios/50/ffffff/email.png")

        st.subheader("hoteLuxury@gmail.com")
    st.caption("NOM et PRENOMS: Bouhssous Mouad / Atraoui Doha // / /")