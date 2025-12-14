import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from datetime import datetime, timedelta

st.set_page_config(page_title="Accueil")
#Sidebar with hamburger menu#

st.markdown(
    """
    <style>
    /* Change app background */
    [data-testid="stHeader"]{
    background-color:rgba(255,255,255,0);
    
    }
    #hotel-luxury{
    font-size:60px;
    margin-top:150px;
    margin-left:150px;
    font-family:serif;
    color:white;
    }
    [data-testid="stAppViewContainer"] {
        background-image:  linear-gradient(155deg, rgba(12, 13, 20, 0.200) 0%, rgba(2, 3, 3, 0.500) 100%),url("https://wallpapercave.com/wp/wp12814430.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        height: 100%;
        
    }
    [data-test-script-state="initial"]{
    background-color:rgb(255,255,255);

    }

    /* Change sidebar background */
    [data-testid="stSidebar"] {
        background-color: black;
    }
    #les-caracteristiques-de-notre-hotel{
    margin-top:500px;
    }
    [data-testid="stHorizontalBlock"]{
    margin-bottom:200px;
    }
    h3{
    font-size:20px
    }
    h3{
    font-size:20px
    }
    </style>
    """,
    unsafe_allow_html=True
)
#collapsible effect#
main_container = st.container()
with main_container:
  st.title("Hotel Luxury\n\n\n\n\n")
  #st.write("caracteristique Principale:")
  st.title("Les caractéristiques de notre hôtel")
# Créer 3 colonnes
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
# Section Actualités / Promotions
st.markdown(
    """
    <div style="
        background: rgba(0, 0, 0, 0.3);  /* fond semi-transparent noir pour rester dans le thème */
        padding: 20px;
        border-radius: 15px;
        margin-top: 40px;
        margin-bottom: 100px;
        color: white;
    ">
        <h3>🔥 Offres spéciale ce mois !</h3>
        <p>Profitez de -20% sur les suites ce mois-ci !</p>
        <p>Accès gratuit au spa pour toute réservation de plus de 3 nuits!</p>
        <p>Réservez votre séjour avec un dîner offert pour deux personnes.</p>
    </div>
    """,
    unsafe_allow_html=True
)
st.write("Contactez-nous:")
contact,facebook,phone,email=st.columns(4)
with contact:
    st.markdown(
        '[![Instagram](https://img.icons8.com/ios/50/ffffff/instagram.png)](https://www.instagram.com/hotel_luxury)',
        unsafe_allow_html=True
    )
    st.subheader("Instagram")
with facebook:
    st.markdown(
        '[![Facebook](https://img.icons8.com/ios/50/ffffff/facebook.png)](https://www.facebook.com/hotel_luxury)',
        unsafe_allow_html=True
    )
    st.subheader("Facebook")

with phone:
    st.image("https://img.icons8.com/ios/50/ffffff/phone.png")
    st.subheader("+212 05 99 99 99 99")

with email:
    st.markdown(
        '[![Email](https://img.icons8.com/ios/50/ffffff/email.png)](mailto:hoteLuxury@gmail.com)',
        unsafe_allow_html=True
    )
    st.subheader("hoteLuxury@gmail.com")
#tetstimonials section
st.markdown("---")
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

st.caption("NOM et PRENOMS: **********************")



