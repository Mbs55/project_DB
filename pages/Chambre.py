import streamlit as st
import pandas as pd

# =========================
# CONFIG PAGE
# =========================
st.set_page_config(
    page_title="Chambres",
    page_icon="🛏️",
    layout="wide"
)

# =========================
# STYLE CSS (BLANC + BEIGE)
# =========================
st.markdown("""
<style>

/* HEADER */
[data-testid="stHeader"]{
    background-color: transparent;
}
   [data-testid="stToolbar"]{
    background-color:transparent;
}

/* SIDEBAR */
[data-testid="stSidebar"]{
    background-color: rgba(0,0,0,0.85);
}

[data-testid="stSidebarContent"]{
        background-color: rgba(0,0,0,0.7);

}
[data-testid="stAppDeployButton"]{
    visibility:hidden;}


[data-testid="stAppViewContainer"] {
    background-image:
        linear-gradient(
            rgba(0,0,0,0.5),
            rgba(0,0,0,0.9)
        ),
        url("https://images.unsplash.com/photo-1566073771259-6a8506099945");
    background-size: cover;
    background-attachment: fixed;
}
    [data-testid="stSidebarHeader"]{
    background-image: url(https://media.istockphoto.com/id/1092200002/vector/luxury-hotel-logo-vector-design-on-black-background.jpg?s=612x612&w=0&k=20&c=GiriWYtD7uai5bf6Ac23IVCE2NKpSc5X3CGf6cUq47U=);
    background-size: cover;
    background-repeat: no-repeat;
    height: 150px; 
    }

/* TITRES */
h1, h2, h3, h4, h5 {
    color: white !important;
    font-weight: 800;
}

/* TEXTE */
p, label, span, li {
    color: #F5F5DC !important;
    font-size: 16px;
}

/* CARTES */
.section {
    background: rgba(0,0,0,0.65);
    padding: 22px;
    border-radius: 18px;
    margin-bottom: 22px;
    border: 1px solid rgba(255,255,255,0.15);
}

/* TABLE */
thead tr th {
    background-color: rgba(0,0,0,0.85) !important;
    color: white !important;
}
tbody tr td {
    color: white !important;
}

/* WIDGETS */
[data-baseweb="radio"] label,
[data-baseweb="checkbox"] label,
[data-baseweb="select"] label {
    color: white !important;
    font-weight: 500;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TITRE PRINCIPAL
# =========================
st.markdown("""
<div style="margin-left:220px;
margin-top:150px;
">
<h1 style="font-family:serif;">🛏️ Gestion des chambres</h1>
<p style="font-size:15px;
margin-bottom:400px;">
Consultez les <b>chambres disponibles</b> avec leurs 
<b>caractéristiques complètes</b> dans un cadre élégant et lisible.
</p>
</div>
""", unsafe_allow_html=True)

# =========================
# IMAGE LUXE SIDEBAR
# =========================
with st.sidebar:
    st.markdown("""
    <div style="
        background-image: url('https://images.unsplash.com/photo-1566073771259-6a8506099945');
        background-size: cover;
        background-position: center;
        height: 260px;
        border-radius: 18px;
        margin-bottom: 25px;
        position: relative;
    ">
        <div style="
            position: absolute;
            bottom: 0;
            width: 100%;
            padding: 15px;
            background: rgba(0,0,0,0.6);
            border-radius: 0 0 18px 18px;
        ">
            <h3 style="color:white; margin:0;">Luxury Hotel</h3>
            <p style="color:#F5F5DC; font-size:14px; margin:0;">
                Comfort • Elegance • Prestige
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# =========================
# CONNEXION DB
# =========================
conn = st.connection("hotel")
query = """select CodR,FLOOR,SurfaceArea,Type from ROOM """

query1 = """
SELECT 
    r.CodR AS code_c,
    r.Floor AS etage,
    r.SurfaceArea AS surface,
    r.Type as type_chambre,
    GROUP_CONCAT(DISTINCT a.AMENITIES_Amenity SEPARATOR ', ') AS equipements,
    GROUP_CONCAT(DISTINCT s.SPACES_Space SEPARATOR ', ') AS espaces
FROM ROOM r
LEFT JOIN HAS_AMENITIES a ON r.CodR = a.ROOM_CodR
LEFT JOIN HAS_SPACES s ON r.CodR = s.ROOM_CodR
GROUP BY r.CodR, r.Floor, r.SurfaceArea;
"""

df = conn.query(query1)
col1, col2, col3 = st.columns(3)
with col1:
    type_filter = st.radio(
        "Type de chambre",
        ["Toutes", "Simple", "Double", "Triple", "Suite"]
    )

# multiselect : équipements (balcony, minibar, etc.)
df_amen = conn.query("SELECT DISTINCT AMENITIES_Amenity FROM HAS_AMENITIES;")
amenities_list = df_amen["AMENITIES_Amenity"].tolist()

with col2:
    equipementss = st.multiselect(
        "Équipements souhaités",
        options=amenities_list
    )

# checkbox : présence d'une cuisine
with col3:
    cuisine = st.checkbox("🍳 Avec cuisine")

st.subheader("📋 Chambres disponibles")
st.divider()


#FR -> EN pour ROOM.Type
type_map = {
    "Simple": "single",
    "Double": "double",
    "Triple": "triple",
    "Suite": "suite"
}

# filtre type
if type_filter != "Toutes":
    room_type = type_map[type_filter]
    df = df[df["type_chambre"] == room_type]

# filtre équipements (tous ceux choisis doivent apparaître)
if equipementss:
    for e in equipementss:
        # .str.contains(e) pour vérifier la présence de l'équipement dans la chaîne
        df = df[df["equipements"].fillna("").str.contains(e)]

# filtre cuisine (SPACES_Space = 'kitchen')
if cuisine:
    df = df[df["espaces"].fillna("").str.contains("kitchen")]


st.dataframe(df[["code_c", "etage", "surface", "type_chambre"]])

# =========================
# IMAGES PAR TYPE
# =========================
images = {
    "single": "https://www.arcotel-acaciasetoile.com/wp-content/uploads/2019/06/chambre-single-acacias-etoile-312-b-1260x969.jpg",
    "double": "https://www.gurtenpark.ch/media/volgxgue/headerbild_hotel_1920x1080_.jpg?width=1920&v=1dc0de825e9df10",
    "triple": "https://hotelidouanfacasablanca.com/assets/img/hotelidouanfa-casablanca/chambres/triple/chambre-triple-slider001-min.jpg",
    "suite": "https://previews.123rf.com/images/drixe/drixe2306/drixe230600012/205818670-modern-luxury-bedroom-interior-design-with-brown-marble-walls-wooden-floor-comfortable-king-size.jpg"
}

# =========================
# APERÇU VISUEL
# =========================
st.subheader("🏨 Aperçu des chambres")
df = conn.query(query1)

for _, row in df.head(5).iterrows():
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown(f"""
        <div class="section">
            <h3>Chambre {row.code_c} — {row.type_chambre}</h3>
            <p><b>Étage :</b> {row.etage}</p>
            <p><b>Surface :</b> {row.surface} m²</p>
            <p><b>Équipements :</b> {row.equipements or "Aucun"}</p>
            <p><b>Espaces :</b> {row.espaces or "—"}</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.image(images[row.type_chambre], use_container_width=True)

st.divider()