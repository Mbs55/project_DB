import streamlit as st

def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        st.markdown('<div class="agence-page">', unsafe_allow_html=True)

        # ------------------ Scoped CSS for agence page ------------------
        st.markdown("""
          <style>
          /* Reset homepage styles (optional) */
          .home-page [data-testid="stAppViewContainer"],
          .home-page h3,
          .home-page #hotel-luxury {
              all: unset;
          }

          /* Agence page styles */
          .agence-page [data-testid="stAppViewContainer"] {
              background-image: linear-gradient(155deg, rgba(12, 13, 20, 0.2) 0%, rgba(2,3,3,0.5) 100%), url("https://wallpapercave.com/wp/wp12814430.jpg");
              background-size: cover;
              background-repeat: no-repeat;
              background-attachment: fixed;
              height: 100%;
          }

          .agence-page h1, .agence-page h2, .agence-page h3 {
              color: white;
          }

          .agence-page [data-testid="stMetric"]{
              border-radius: 15px;
              background-color: rgba(118, 107, 129, 0.4);
              color: brown;
          }

          #map_div{
              margin-bottom:100px;
          }

          #nos-agences{
              margin-top:500px;
          }

          </style>
          """, unsafe_allow_html=True)
