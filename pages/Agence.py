import streamlit as st
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
        st.success(f"Agences disponibles à {ville}")
        st.dataframe(result)
    else:
        st.warning("Aucune agence trouvée")

st.divider()

# ======================= ALL AGENCIES =======================
st.header("Nos agences")

all_agences = conn.query("""
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
    FROM TRAVEL_AGENCY;
""")

for i in range(min(4, len(all_agences))):
    cols = st.columns([4, 1])
    with cols[0]:
        st.subheader(f"Agence {all_agences.iloc[i]['CodA']}")
        st.write("📍 Adresse :", all_agences.iloc[i]["adresse_complete"])
        st.write("💻 Site web :", all_agences.iloc[i]["WebSite"])
        st.write("📞 Téléphone :", all_agences.iloc[i]["Tel"])
    with cols[1]:
        st.image(f"./assets/image{i}.webp", width=250)
    st.divider()

with st.expander("Voir plus"):
    for i in range(4, len(all_agences)):
        st.write("🏢 Agence", all_agences.iloc[i]["CodA"])
        st.write("📍", all_agences.iloc[i]["adresse_complete"])
        st.write("📞", all_agences.iloc[i]["Tel"])
        st.divider()
