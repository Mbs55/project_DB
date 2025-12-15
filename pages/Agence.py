import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
import folium
st.set_page_config(page_title="AGENCES", layout="wide")




st.markdown("""
    <style>

    [data-testid="stHeader"]{
                background-color:rgba(255,255,255,0);
                }
     [data-testid="stMetric"]{
                border-radius: 15px;
                background-color:rgba(118, 107, 129, 0.4);
                }            

    [data-testid="stAppViewContainer"] {
                    background-image:  linear-gradient(155deg, rgba(12, 13, 20, 0.200) 0%, rgba(2, 3, 3, 0.500) 100%),url("https://wallpapercave.com/wp/wp12814430.jpg");
                    background-size: cover;
                    background-repeat: no-repeat;
                    background-attachment: fixed;
                    height: 100%;}

    #map_div{
                    margin-bottom:300px;

                }
    #consultez-nos-agences{
    font-size:60px;
    margin-top:150px;
    margin-left:200px;
    font-family:serif;
    color:white;
    margin-bottom:400px;
    
    }            
    [data-testid="stHorizontalBlock"]{
    margin-bottom:100px;
    
    }
    
                </style>                


    """, unsafe_allow_html=True)
st.title("Consultez Nos agences : \n\n")
# **********************************Question 1:***********************
conn = st.connection(name="hotel")
query = conn.query("select count(distinct code_a) from AGENCE_DE_VOYAGE;")
query2 = conn.query("select count(distinct nom_ville) from VILLE ;")
query3 = conn.query("select nom_ville,count(*) as compteur from AGENCE_DE_VOYAGE group by nom_ville order by 2;")
a, b, c = st.columns(3)
df = pd.DataFrame(query3)
query3 = df.iloc[-1]
with a:
    st.subheader("Nos Agences de Voyage")
    st.write("Plusieurs établissements, une seule signature hôtelière:\n")
    a.metric("Nombre d' agence:", query["count(distinct code_a)"], border=True)

with b:
    st.subheader("Réseau étendu:")
    st.write("Le confort et le service de notre hôtel, où que vous soyez")
    b.metric("Nombre de ville:", query2["count(distinct nom_ville)"], border=True)


with c:
    st.subheader("Forte présence")
    st.write("Présent avec plusieurs agences hôtelières dans la ville:")
    c.metric(f"La Ville {query3["nom_ville"]} :", query3["compteur"], border=True)

# ***********************************Question 2:MAP**********************
st.divider()
st.header("Carte:")
m = folium.Map(location=[34.020882, -6.841650], zoom_start=8)
query4 = conn.query(
        "select VILLE.longi,VILLE.latit from VILLE,AGENCE_DE_VOYAGE where AGENCE_DE_VOYAGE.nom_ville=VILLE.nom_ville;")
df = pd.DataFrame(query4)
for i in range(len(df)):
    folium.Marker(location=[df.loc[i]["latit"], df.loc[i]["longi"]], icon=folium.Icon(
            icon="map-marker",
            prefix="fa",
            color="red"
        )).add_to(m)

st_data = st_folium(m, width="70%")
st.divider()

#****************************************************************
st.header("🔍 Rechercher des agences par ville")
ville_recherche = st.text_input("Entrez le nom de la ville :")

if ville_recherche:
        query_ville = conn.query(
            """
            SELECT 
                code_a,
                site_web,
                telephone,
                CONCAT(nom_ville,' ',rue_a,' ',num_a,' ',code_postal,' ',pays_a) AS adresse_complete
            FROM AGENCE_DE_VOYAGE
            WHERE LOWER(nom_ville) = LOWER(:ville)
            """,
            params={"ville": ville_recherche}
        )

        if len(query_ville) > 0:
            st.success(f"Agences disponibles à {ville_recherche} :")
            st.write(query_ville)
        else:
            st.warning(f"Aucune agence trouvée dans la ville : {ville_recherche}")
st.divider()
# *************************************Question 3:*********************************
query5 = conn.query(
        "select code_a,site_web,telephone,concat(nom_ville,' ',rue_a,' ',num_a,' ',code_postal,' ',pays_a) as adresse_complete from AGENCE_DE_VOYAGE;")
st.header("Nos agences:")
for i in range(4):
    cols = st.columns([4, 1])
    with cols[0]:
        st.subheader("Nom de l'agence:", query5.iloc[i]["code_a"])
        st.write("📍 Adresse:", query5.iloc[i]["adresse_complete"])
        st.write("💻 Pour Plus d informations Visiter le Site Web: ", query5.iloc[i]["site_web"])
        st.write("📞 Contactez-nous:", query5.iloc[i]["telephone"])
    with cols[1]:
        st.image(f"./assets/image{i}.webp", width=300)
    st.divider()

with st.expander("Plus", expanded=False):
    for i in range(4, len(query5)):
        cols = st.columns([4])
        with cols[0]:
            st.subheader("Nom de l'agence:", query5.iloc[i]["code_a"])
            st.write("📍 Adresse:", query5.iloc[i]["adresse_complete"])
            st.write("💻 Pour Plus d informations Visiter le Site Web: ", query5.iloc[i]["site_web"])
            st.write("📞 Contactez-nous:", query5.iloc[i]["telephone"])
st.divider()

# ************* Question 4 :*************




