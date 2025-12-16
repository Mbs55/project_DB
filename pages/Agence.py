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
    [data-testid="stSidebarNavLink"] span {
    color:white;
    }            
       [data-testid="stSidebarContent"]{
    border-radius:15px;
    }            
    [data-testid="stSidebarHeader"]{
    background-image: url("./assets/hotel.webp");
    background-size: cover;
    background-repeat: no-repeat; 
    }
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
query = conn.query("select count(CodA) from TRAVEL_AGENCY;")
query2 = conn.query("select count(Name) from CITY ;")
query3 = conn.query("select City_Address,count(*) as compteur from TRAVEL_AGENCY group by City_Address order by 2;")
a, b, c = st.columns(3)
df = pd.DataFrame(query3)
query3 = df.iloc[-1]
with a:
    st.subheader("Nos Agences de Voyage")
    st.write("Plusieurs établissements, une seule signature hôtelière:\n")
    a.metric("Nombre d' agence:", query["count(CodA)"], border=True)

with b:
    st.subheader("Réseau étendu:")
    st.write("Le confort et le service de notre hôtel, où que vous soyez")
    b.metric("Nombre de ville:", query2["count(Name)"], border=True)


with c:
    st.subheader("Forte présence")
    st.write("Présent avec plusieurs agences hôtelières dans la ville:")
    c.metric(f"La Ville {query3["City_Address"]} :", query3["compteur"], border=True)













# ***********************************Question 2:MAP**********************
st.divider()
st.header("📍 Carte De Nos Agences:")
m = folium.Map(location=[34.020882, -6.841650], zoom_start=8)
query4 = conn.query("select CITY.Longitude,CITY.Latitude from CITY,TRAVEL_AGENCY where TRAVEL_AGENCY.City_Address=CITY.Name;")
df = pd.DataFrame(query4)
for i in range(len(df)):
    folium.Marker(location=[df.loc[i]["Latitude"], df.loc[i]["Longitude"]], icon=folium.Icon(
            icon="map-marker",
            prefix="fa",
            color="red"
        )).add_to(m)
st_data = st_folium(m, width="70%")
st.divider()
















st.header("🔍 Recherche Des Agences par Ville")
ville_recherche = st.text_input("Entrez le Nom de la ville :")

if ville_recherche:
        query_ville = conn.query(
            """
            SELECT 
                CodA,
                WebSite,
                Tel,
                CONCAT(City_Address,' ',Street_Address,' ',Num_Address,' ',ZIP_Address,' ',Country_Address) AS adresse_complete
            FROM TRAVEL_AGENCY
            WHERE LOWER(Country_Address) = LOWER(:ville)
            """,
            params={"ville": ville_recherche}
        )

        if len(query_ville) > 0:
            st.success(f"Agences disponibles à {ville_recherche} :")
            st.dataframe(query_ville)
        else:
            st.warning(f"Aucune agence trouvée dans la ville : {ville_recherche}")
st.divider()
# *************************************Question 3:*********************************














query5 = conn.query(
        "select CodA,WebSite,Tel,CONCAT(City_Address,' ',Street_Address,' ',Num_Address,' ',ZIP_Address,' ',Country_Address) AS adresse_complete from TRAVEL_AGENCY;")
st.header("Nos agences:")
for i in range(4):
    cols = st.columns([4, 1])
    with cols[0]:
        st.write("Code D'Agence:", query5.iloc[i]["CodA"])
        st.write("📍 Adresse:", query5.iloc[i]["adresse_complete"])
        st.write("💻 Pour Plus d informations Visiter le Site Web: ", query5.iloc[i]["WebSite"])
        st.write("📞 Contactez-nous:", query5.iloc[i]["Tel"])
    with cols[1]:
        st.image(f"./assets/image{i}.webp", width=300)
    st.divider()
with st.expander("Plus", expanded=False):
    for i in range(4, len(query5)):
        cols = st.columns([4])
        with cols[0]:
            st.write("code de l'agence:", query5.iloc[i]["CodA"])
            st.write("📍 Adresse:", query5.iloc[i]["adresse_complete"])
            st.write("💻 Pour Plus d informations Visiter le Site Web: ", query5.iloc[i]["WebSite"])
            st.write("📞 Contactez-nous:", query5.iloc[i]["Tel"])
st.divider()




