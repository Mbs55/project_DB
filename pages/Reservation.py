import streamlit as st
import pandas as pd

st.set_page_config(page_title="reservation", layout="wide")

st.markdown("""
    <style>
        /* Styles généraux pour l'arrière-plan et la cohérence */
        [data-testid="stHeader"] {
            background-color: rgba(255,255,255,0);
        }
        [data-testid="stMetric"] {
            border-radius: 15px;
            background-color: rgba(118, 107, 129, 0.4);
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        }
        [data-testid="stSidebarNavLink"] span {
            color: white;
        }
        [data-testid="stSidebarContent"] {
            border-radius: 15px;
        }
        [data-testid="stSidebarHeader"] {
            background-image: url("https://media.istockphoto.com/id/1092200002/vector/luxury-hotel-logo-vector-design-on-black-background.jpg?s=612x612&w=0&k=20&c=GiriWYtD7uai5bf6Ac23IVCE2NKpSc5X3CGf6cUq47U=");
            background-size: cover;
            background-repeat: no-repeat;
            height: 150px;
            border-radius: 15px;
            margin-bottom: 70px;
        }
        [data-testid="stSidebar"] {
            background-color: rgba(3,3,0,0.7);
        }
        [data-testid="stAppViewContainer"] {
            background-image: linear-gradient(155deg, rgba(12, 13, 20, 0.200) 0%, rgba(2, 3, 3, 0.500) 100%), url("https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?ixlib=rb-4.0.3&auto=format&fit=crop&w=2070&q=80");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            height: 100%;
        }
        #map_div {
            margin-bottom: 300px;
        }
        #consultez-nos-agences {
            font-size: 60px;
            margin-top: 150px;
            margin-left: 200px;
            font-family: serif;
            color: white;
            margin-bottom: 400px;
        }
        [data-testid="stHorizontalBlock"] {
            margin-bottom: 100px;
        }

        /* Améliorations pour les titres et texte */
        h1, h2, h3, h4, h5 {
            color: white !important;
            font-weight: 800;
            text-align: center;  /* Centrer les titres pour un look plus propre */
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);  /* Ombre pour contraste */
        }
        p, label, span, li {
            color: #F5F5DC !important;  /* Beige pour le texte général */
            font-size: 16px;
        }
        [data-testid="stMetricValue"] div {
            color: white !important;
        }

        /* Améliorations pour les DataFrames : arrière-plan transparent pour montrer la photo */
        [data-testid="stDataFrame"] {
            background: transparent !important;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
            color: white !important;
        }
        [data-testid="stDataFrame"] th, [data-testid="stDataFrame"] td {
            background: transparent !important;
            color: white !important;
            border: 1px solid rgba(255,255,255,0.2);  /* Bordures subtiles */
        }

        /* Améliorations pour les graphiques */
        [data-testid="stPlotlyChart"] {
            background: transparent !important;
            border-radius: 10px;
        }

        /* Centrer les métriques et colonnes */
        .metric-container {
            display: flex;
            justify-content: center;
            align-items: center;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>Tableau de Bord – Réservations</h1>
</div>
""", unsafe_allow_html=True)

<<<<<<< HEAD
st.markdown("Cette page analyse toutes les réservations de l'hôtel .")

conn = st.connection(name="hotel")

# Utiliser st.expander pour organiser et améliorer la lisibilité
with st.expander(" Chambres Disponibles", expanded=True):
    query1 = """
        SELECT
            R.CodR AS ROOM_CodR,
            R.Floor,
            R.SurfaceArea,
            R.Type
        FROM ROOM R
        WHERE R.CodR NOT IN (
            SELECT DISTINCT B.ROOM_CodR
            FROM BOOKING B
        )
        ORDER BY R.CodR;
    """
    df1 = conn.query(query1)
    st.dataframe(df1, use_container_width=True)
=======



st.markdown("Cette page analyse toutes les réservations de l'hôtel.")

conn = st.connection(name="hotel")

st.subheader(" Les Chambres Disponible: ")
>>>>>>> e780dac3fc30be49cb459cad4f6664107af65554

with st.expander(" Chambre avec le Coût Journalier Moyen le Plus Élevé par Mois"):
    query9 = """
    SELECT
<<<<<<< HEAD
        mois,
        CodR,
        Floor,
        SurfaceArea,
        Type,
        cout_journalier_moyen
    FROM (
        SELECT
            EXTRACT(MONTH FROM B.StartDate) AS mois,
            R.CodR,
            R.Floor,
            R.SurfaceArea,
            R.Type,
            ROUND(AVG(B.Cost / DATEDIFF(B.EndDate,B.StartDate)), 2) AS cout_journalier_moyen,
            RANK() OVER (
                PARTITION BY EXTRACT(MONTH FROM B.StartDate)
                ORDER BY AVG(B.Cost / DATEDIFF(B.EndDate, B.StartDate)) DESC
            ) AS rang
        FROM BOOKING B
        JOIN ROOM R ON R.CodR = B.ROOM_CodR
        GROUP BY mois, R.CodR, R.Floor, R.SurfaceArea, R.Type
    ) t
    WHERE rang = 1
=======
    R.CodR AS ROOM_CodR,
    R.Floor,
    R.SurfaceArea,
    R.Type
    FROM ROOM R
    WHERE R.CodR NOT IN (
    SELECT DISTINCT B.ROOM_CodR
    FROM BOOKING B
)
ORDER BY R.CodR;

"""
df1 = conn.query(query1)

st.dataframe(df1, use_container_width=True)
st.markdown("---")
query="""
SELECT mois, ROOM_CodR, FLOOR,SurfaceArea,Type,prix_journalier AS Prix_Journalier
FROM (
    SELECT
        EXTRACT(MONTH FROM StartDate) AS mois,
        ROOM_CodR,
        AVG(Cost / NULLIF(DATEDIFF(EndDate, StartDate), 0)) AS prix_journalier,
        RANK() OVER (
            PARTITION BY EXTRACT(MONTH FROM StartDate)
            ORDER BY AVG(Cost / NULLIF(DATEDIFF(EndDate, StartDate), 0)) DESC
        ) AS rnk
    FROM BOOKING
    GROUP BY mois, ROOM_CodR
) t,ROOM where ROOM.CodR=t.ROOM_CodR and rnk = 1
ORDER BY mois;
"""
st.subheader(" Chambre avec le Coût Journalier Moyen le Plus Élevé par Mois")

df_top = conn.query(query)

st.dataframe(df_top, use_container_width=True)
st.markdown("---")

# Prix moyen par mois
st.subheader("Prix moyen par mois")

query2 = """
    SELECT 
        EXTRACT(MONTH FROM StartDate) AS mois,
        ROUND(AVG(Cost), 2) AS prix_moyen
    FROM BOOKING
    GROUP BY mois
>>>>>>> e780dac3fc30be49cb459cad4f6664107af65554
    ORDER BY mois;
    """
    df_top = conn.query(query9)
    st.dataframe(df_top, use_container_width=True)

with st.expander(" Évolution du Coût Journalier Moyen par Mois"):
    query10 = """
        SELECT
            EXTRACT(MONTH FROM StartDate) AS mois,
            ROUND(AVG(Cost / DATEDIFF(EndDate,StartDate)), 2) AS cout_journalier_moyen
        FROM BOOKING
        GROUP BY EXTRACT(MONTH FROM StartDate)
        ORDER BY mois;
    """
    df_cout = conn.query(query10)
    st.line_chart(df_cout.set_index("mois"))

with st.expander(" Prix Moyen par Mois"):
    query2 = """
        SELECT 
            EXTRACT(MONTH FROM StartDate) AS mois,
            ROUND(AVG(Cost), 2) AS prix_moyen
        FROM BOOKING
        GROUP BY EXTRACT(MONTH FROM StartDate)
        ORDER BY mois;
    """
    df2 = conn.query(query2)
    st.line_chart(df2.set_index("mois"))

with st.expander(" Revenus Totaux par Agence"):
    query3 = """
        SELECT 
            TRAVEL_AGENCY_CodA,
            SUM(Cost) AS revenu_total
        FROM BOOKING
        GROUP BY TRAVEL_AGENCY_CodA
        ORDER BY revenu_total DESC;
    """
    df3 = conn.query(query3)
    col1, col2 = st.columns(2)
    with col1:
        st.dataframe(df3, use_container_width=True)
    with col2:
        st.bar_chart(df3.set_index("TRAVEL_AGENCY_CodA"))

with st.expander(" Chambre la Plus Réservée"):
    query4 = """
        SELECT 
            ROOM_CodR,
            COUNT(*) AS nb_reservations
        FROM BOOKING
        GROUP BY ROOM_CodR
        ORDER BY nb_reservations DESC
        LIMIT 1;
    """
    df4 = conn.query(query4)
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Chambre la plus réservée", df4["ROOM_CodR"][0])
    with col2:
        st.metric("Nombre de réservations", df4["nb_reservations"][0])

st.subheader(" Durée Moyenne des Séjours")
query5 = """
SELECT 
    ROUND(AVG(DATEDIFF(EndDate, StartDate))) AS duree_moyenne
FROM BOOKING;
"""

df5 = conn.query(query5)
st.metric("Durée moyenne (jours)", df5["duree_moyenne"][0])
st.markdown("---")

with st.expander(" Nombre de Réservations par Mois"):
    query6 = """
        SELECT
            EXTRACT(MONTH FROM StartDate) AS mois,
            COUNT(*) AS nb_reservations
        FROM BOOKING
        GROUP BY EXTRACT(MONTH FROM StartDate)
        ORDER BY mois;
    """
    df6 = conn.query(query6)
    st.bar_chart(df6.set_index("mois"))

with st.expander(" Chambre la Plus Rentable"):
    query7 = """
        SELECT
            ROOM_CodR,
            SUM(Cost) AS revenu_total
        FROM BOOKING
            GROUP BY ROOM_CodR
        ORDER BY revenu_total DESC
        LIMIT 1;
    """
    df7 = conn.query(query7)
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Chambre la plus rentable", df7["ROOM_CodR"][0])
    with col2:
        st.metric("Revenu total (DH)", df7["revenu_total"][0])

<<<<<<< HEAD
with st.expander(" Nombre Total de Jours Réservés par Agence"):
    query8 = """
        SELECT 
            TRAVEL_AGENCY_CodA,
            SUM(DATEDIFF(B.EndDate, B.StartDate)) AS jours_reserves
        FROM BOOKING B
        GROUP BY TRAVEL_AGENCY_CodA
        ORDER BY jours_reserves DESC;
    """
    df8 = conn.query(query8)
    col1, col2 = st.columns(2)
    with col1:
        st.dataframe(df8, use_container_width=True)
    with col2:
        st.bar_chart(df8.set_index("TRAVEL_AGENCY_CodA"))
=======
df6 = conn.query(query6)
st.bar_chart(df6.set_index("mois"))
st.markdown("---")

# Chambre la plus rentable
st.subheader(" Chambre la Plus Rentable")

query7 = """
SELECT
    ROOM_CodR,
    SUM(Cost) AS revenu_total
FROM BOOKING
GROUP BY ROOM_CodR
ORDER BY revenu_total DESC
LIMIT 1;
"""

df7 = conn.query(query7)

col1, col2 = st.columns(2)
col1.metric("Chambre la plus rentable", df7["ROOM_CodR"][0])
col2.metric("Revenu total (DH)", df7["revenu_total"][0])

st.markdown("---")

# Jours réservés par agence
st.subheader(" Nombre Total de Jours Réservés par Agence")

query8 = """
SELECT 
    TRAVEL_AGENCY_CodA,
    SUM(DATEDIFF(EndDate, StartDate)) AS jours_reserves
FROM BOOKING
GROUP BY TRAVEL_AGENCY_CodA
ORDER BY jours_reserves DESC;
"""

df8 = conn.query(query8)
col1, col2 = st.columns(2)
col1.dataframe(df8, use_container_width=True)
col2.bar_chart(df8.set_index("TRAVEL_AGENCY_CodA"))

st.markdown("---")
query10 = """SELECT
    EXTRACT(MONTH FROM StartDate) AS mois,
    ROUND(AVG(Cost / DATEDIFF(EndDate, StartDate)), 2) AS cout_journalier_moyen
FROM BOOKING
GROUP BY EXTRACT(MONTH FROM StartDate)
ORDER BY mois;
"""
st.subheader("Évolution du Coût Journalier Moyen par Mois")

df_cout = conn.query(query10)

st.line_chart(df_cout.set_index("mois"))
st.markdown("---")
>>>>>>> e780dac3fc30be49cb459cad4f6664107af65554
