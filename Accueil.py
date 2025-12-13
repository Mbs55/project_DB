import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Accueil")

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
    margin-bottom:500px;
    }
    h3{
    font-size:20px
    }
    </style>
    """,
    unsafe_allow_html=True
)
#Layout with collapsible effect#
st.title("Hotel Luxury\n\n\n\n\n")
#st.write("caracteristique Principale:")
st.title("Les caractéristiques de notre hôtel")

# Créer 3 colonnes
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://img.icons8.com/ios-filled/50/ffffff/swimming-pool.png")
    st.subheader("Piscine")
    st.write("Détendez-vous dans notre piscine luxueuse.")

with col2:
    st.image("https://img.icons8.com/ios/50/ffffff/spa.png")
    st.subheader("Spa & Bien-être")
    st.write("Reposez votre esprit et votre corps.")

with col3:
    st.image("https://img.icons8.com/ios/50/ffffff/restaurant.png")
    st.subheader("Restauration")
    st.write("Profitez d'expériences culinaires raffinées.")


st.write("Contactez-nous:")
contact,facebook,phone,email=st.columns(4)
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


st.caption("NOM et PRENOMS: **********************")


