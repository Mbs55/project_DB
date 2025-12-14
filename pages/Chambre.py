import streamlit as st
import pandas as pd

# PAGE CHAMBRES

st.set_page_config(
    page_title="Chambres",
    page_icon="🛏️",
    layout="wide"
)

st.markdown("""
<style>
/* En-tête transparent */
[data-testid="stHeader"]{
    background-color: rgba(255,255,255,0);
}

/* Fond principal avec overlay plus lisible */
[data-testid="stAppViewContainer"] {
    background-image: linear-gradient(
        155deg,
        rgba(12, 13, 20, 0.55) 3%,
        rgba(2, 3, 3, 0.85) 100%
    ),
    url("https://images.unsplash.com/photo-1566073771259-6a8506099945");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    color: white;
}

/* Titres : hiérarchie claire */
h1 {
    color: #E76F51;
    font-weight: 800;
}

h2 {
    color: #2A9D8F;
    font-weight: 700;
}

h3, h4 {
    color: white;
}

/* Texte général */
p, label {
    color: #F1FAEE;
    font-size: 16px;
    color: white;
}

/* Sections / cartes */
.section {
    background: rgba(0, 0, 0, 0.55);
    padding: 25px;
    border-radius: 16px;
    margin-bottom: 25px;
    color: white;
}

/* Widgets (radio, checkbox, selectbox) */
[data-baseweb="radio"] label,
[data-baseweb="checkbox"] label,
[data-baseweb="select"] label {
    color: #F1FAEE !important;
    font-weight: 500;
}

/* Badge type chambre (optionnel) */
.badge {
    padding: 6px 12px;
    border-radius: 10px;
    color: white;
    font-weight: 600;
    display: inline-block;
    margin-bottom: 8px;
}
</style>

""", unsafe_allow_html=True)


st.title("🛏️ Gestion des chambres")
st.markdown("""
Cette page permet de **consulter et filtrer les chambres disponibles** de la chaîne hôtelière.
Chaque chambre est identifiée par un **code unique**, un **étage**, une **superficie**, un **type**
(simple, double, triple ou suite) et une **liste d’équipements**.
Les suites disposent en plus de **plusieurs espaces**.
""")

# CONNEXION MYSQL
conn = st.connection("hotel")

# REQUÊTE SQL
query = """
SELECT 
    c.code_c,
    c.etage,
    c.surface,
    c.type_chambre,
    GROUP_CONCAT(DISTINCT e.equipement SEPARATOR ', ') AS equipements,
    GROUP_CONCAT(DISTINCT h.espace_dispo SEPARATOR ', ') AS espaces
FROM CHAMBRE c
LEFT JOIN CHAMBRE_EQUIPMENT e ON c.code_c = e.code_c
LEFT JOIN HAS_ESPACE_DISPO h ON c.code_c = h.code_c
GROUP BY c.code_c, c.etage, c.surface, c.type_chambre
"""
df = conn.query(query)



# FILTRES

st.subheader("🔍 Filtres des chambres")

with st.expander("Options de filtrage", expanded=True):

    col1, col2, col3 = st.columns(3)

    with col1:
        type_filter = st.radio(
            "Type de chambre",
            ["Toutes", "Simple", "Double", "Triple", "Suite"]
        )

    with col2:
        equipements = st.multiselect(
            "Équipements souhaités",
            ["TV", "Climatisation", "Mini-bar", "Balcon", "Jacuzzi", "Cuisine équipée"]
        )

    with col3:
        cuisine = st.checkbox("Avec cuisine")


# APPLICATION DES FILTRES

if type_filter != "Toutes":
    df = df[df["type_chambre"] == type_filter]

if equipements:
    df = df[df["equipements"].str.contains('|'.join(equipements), na=False)]

if cuisine:
    df = df[df["equipements"].str.contains("Cuisine", na=False)]

if df.empty:
    st.warning("Aucune chambre ne correspond aux critères sélectionnés.")
    st.stop()

# TABLEAU DES CHAMBRES

st.subheader("📋 Chambres disponibles")

st.dataframe(
    df[["code_c", "etage", "surface", "type_chambre"]],
    use_container_width=True
)

# APERÇU VISUEL (MAX 5 CHAMBRES)

st.subheader("🏨 Aperçu des chambres")

for index, row in df.head(5).iterrows():
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown(f"### Chambre {row['code_c']}")
        st.write(f"**Étage :** {row['etage']}")
        st.write(f"**Surface :** {row['surface']} m²")
        st.write(f"**Type :** {row['type_chambre']}")
        equip_list = row["equipements"].split(", ") if row["equipements"] else []
        for eq in equip_list:
            st.markdown(f"- ✅ {eq}")


        if row["type_chambre"] == "Suite":
            st.write(f"**Espaces disponibles :** {row['espaces']}")

    with col2:
        if row["type_chambre"] == "Simple":
            st.image("https://images.unsplash.com/photo-1505691938895-1758d7feb511")
        elif row["type_chambre"] == "Double":
            st.image("https://images.unsplash.com/photo-1501117716987-c8e1ecb210c9")
        elif row["type_chambre"] == "Triple":
            st.image("https://images.unsplash.com/photo-1560066984-138dadb4c035")
        else:
            st.image("https://images.unsplash.com/photo-1582719478250-c89cae4dc85b")

    st.divider()
