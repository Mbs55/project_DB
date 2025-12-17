import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
import folium

st.set_page_config(page_title="AGENCES", layout="wide")

st.markdown("""import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
import folium

st.set_page_config(page_title="AGENCES", layout="wide")

# ======================= STYLE =======================
st.markdown("""
<style>
[data-testid="stHeader"]{
    background-color:rgba(255,255,255,0);
}
[data-testid="stMetric"]{
    border-radius: 15px;
    background-color:rgba(118, 107, 129, 0.4);
}
h1, h2, h3, h4, h5 {
    color: white !important;
    font-weight: 800;
}
p, label, span, li {
    color: #F5F5DC !important;
    font-size: 16px;
}
[data-testid="stAppViewContainer"] {
    background-image: linear-gradient(
        155deg,
        rgba(12, 13, 20, 0.2) 0%,
        rgba(2, 3, 3, 0.5) 100%
    ),
    url("https://wallpapercave.com/wp/wp12814430.jpg");
    background-size: cover;
    background-attachment: fixed;
}
</style>
""", unsafe_allow_html=True)

st.title("Consultez Nos Agences")

# ======================= DB CONNECTION =======================
conn = st.connection("hotel")

# ======================= METRICS =======================
query_agences = conn.query("SELECT COUNT(CodA) AS nb FROM TRAVEL_AGENCY;")
query_villes = conn.query("SELECT COUNT(Name) AS nb FROM CITY;")
query_top_ville = conn.query("""
    SELECT City_Address, COUNT(*) AS compteur
    FROM TRAVEL_AGENCY
    GROUP BY City_Address
    ORDER BY compteur DESC;
""")

a, b, c = st.columns(3)

with a:
    st.metric("Nombre d'agences", query_agences.iloc[0]["nb"])

with b:
    st.metric("Nombre de villes", query_villes.iloc[0]["nb"])

with c:
    top = query_top_ville.iloc[0]
    st.metric(f"Ville la plus présente : {top['City_Address']}", top["compteur"])

st.divider()

# ======================= MAP =======================
st.header("📍 Carte de nos agences")

coords = conn.query("""
    SELECT CITY.Latitude, CITY.Longitude
    FROM CITY
    JOIN TRAVEL_AGENCY
        ON TRAVEL_AGENCY.City_Address = CITY.Name;
""")

df_coords = pd.DataFrame(coords)

m = folium.Map(
    location=[df_coords.iloc[0]["Latitude"], df_coords.iloc[0]["Longitude"]],
    zoom_start=6
)

for _, row in df_coords.iterrows():
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        icon=folium.Icon(icon="map-marker", prefix="fa", color="red")
    ).add_to(m)

st_folium(m, width="70%")

st.divider()

# ======================= SEARCH BY CITY =======================
st.header("🔍 Recherche des agences par ville")

ville = st.text_input("Entrez le nom de la ville")

if ville:
    result = conn.query("""
        SELECT
            CodA,
            WebSite,
            Tel,
            CONCAT(
                City_Address,' ',
                Street_Address,' ',
                Num_Address,' ',
                ZIP_Address,' ',
                Country_Address
            ) AS adresse_complete
        FROM TRAVEL_AGENCY
        WHERE LOWER(City_Address) = LOWER(:ville)
    """, params={"ville": ville})

    if len(result) > 0:
        st.success(f"Agenc
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
<<<<<<< HEAD
st.header("Carte:")
m = folium.Map(location=[34.020882, -6.841650], zoom_start=8)
query4 = conn.query(
    "select VILLE.longi,VILLE.latit from VILLE,AGENCE_DE_VOYAGE where AGENCE_DE_VOYAGE.nom_ville=VILLE.nom_ville;")
=======
st.header("📍 Carte De Nos Agences:")
query4 = conn.query("select CITY.Longitude,CITY.Latitude from CITY,TRAVEL_AGENCY where TRAVEL_AGENCY.City_Address=CITY.Name;")
>>>>>>> ae832c80659a38398bb6c1c7bbff66408c2f5f82
df = pd.DataFrame(query4)
m = folium.Map(location=[df.loc[0]["Latitude"], df.loc[0]["Longitude"]], zoom_start=8)
for i in range(len(df)):
<<<<<<< HEAD
    folium.Marker(location=[df.loc[i]["latit"], df.loc[i]["longi"]], icon=folium.Icon(
        icon="map-marker",
        prefix="fa",
        color="red"
    )).add_to(m)

st_data = st_folium(m, width="70%")
st.divider()

# ****************************************************************
st.header("🔍 Rechercher des agences par ville")
ville_recherche = st.text_input("Entrez le nom de la ville :")

if ville_recherche:
    query_ville = conn.query(
        """
        SELECT code_a,
               site_web,
               telephone,
               CONCAT(nom_ville, ' ', rue_a, ' ', num_a, ' ', code_postal, ' ', pays_a) AS adresse_complete
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
=======
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
            WHERE LOWER(City_Address) = LOWER(:ville)
            """,
            params={"ville": ville_recherche}
        )

        if len(query_ville) > 0:
            st.success(f"Agences disponibles à {ville_recherche} :")
            st.dataframe(query_ville)
        else:
            st.warning(f"Aucune agence trouvée dans la ville : {ville_recherche}")
>>>>>>> ae832c80659a38398bb6c1c7bbff66408c2f5f82
st.divider()
# *************************************Question 3:*********************************














query5 = conn.query(
<<<<<<< HEAD
    "select code_a,site_web,telephone,concat(nom_ville,' ',rue_a,' ',num_a,' ',code_postal,' ',pays_a) as adresse_complete from AGENCE_DE_VOYAGE;")
=======
        "select CodA,WebSite,Tel,CONCAT(City_Address,' ',Street_Address,' ',Num_Address,' ',ZIP_Address,' ',Country_Address) AS adresse_complete from TRAVEL_AGENCY;")
>>>>>>> ae832c80659a38398bb6c1c7bbff66408c2f5f82
st.header("Nos agences:")
for i in range(4):
    cols = st.columns([4, 1])
    with cols[0]:
<<<<<<< HEAD
        st.subheader("Nom de l'agence:", query5.iloc[i]["code_a"])
        st.write("code de l'agence:", query5.iloc[i]["code_a"])
=======
        st.write("Code D'Agence:", query5.iloc[i]["CodA"])
>>>>>>> ae832c80659a38398bb6c1c7bbff66408c2f5f82
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
<<<<<<< HEAD
            st.subheader("Nom de l'agence:", query5.iloc[i]["code_a"])
            st.write("code de l'agence:", query5.iloc[i]["code_a"])
=======
            st.write("code de l'agence:", query5.iloc[i]["CodA"])
>>>>>>> ae832c80659a38398bb6c1c7bbff66408c2f5f82
            st.write("📍 Adresse:", query5.iloc[i]["adresse_complete"])
            st.write("💻 Pour Plus d informations Visiter le Site Web: ", query5.iloc[i]["WebSite"])
            st.write("📞 Contactez-nous:", query5.iloc[i]["Tel"])
st.divider()




