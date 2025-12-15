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

        st.markdown("""
                <style>
                
                /*[data-testid="stHorizontalBlock"]{
                    margin-bottom: 500px;
                    margin-top: 200px;
                }*/
                [data-testid="stAppViewContainer"] {
                    background-image:  linear-gradient(155deg, rgba(12, 13, 20, 0.200) 0%, rgba(2, 3, 3, 0.500) 100%),url("https://wallpapercave.com/wp/wp12814430.jpg");
                    background-size: cover;
                    background-repeat: no-repeat;
                    background-attachment: fixed;
                    height: 100%;

                }
                [data-testid="stMetric"]{
                border-radius: 15px;
                background-color:rgba(118, 107, 129, 0.4);
                color:brown;
                }
                #map_div{
                    margin-bottom:100px;

                }
                #nos-agences{
                    margin-top:500px;
                }
                #hotel-luxury{
                font-size:60px;
                margin-top:90px;
                margin-left:100px;
                font-family:serif;
                color:white;
                }
                p
                {
                font-size:30px;
                }

                </style>
            """, unsafe_allow_html=True)

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
            st.subheader("Plus de la ville:")
            for i in range(4, len(query5)):
                cols = st.columns([4])
                with cols[0]:
                    st.subheader("Nom de l'agence:", query5.iloc[i]["code_a"])
                    st.write("📍 Adresse:", query5.iloc[i]["adresse_complete"])
                    st.write("💻 Pour Plus d informations Visiter le Site Web: ", query5.iloc[i]["site_web"])
                    st.write("📞 Contactez-nous:", query5.iloc[i]["telephone"])
        st.divider()


st.markdown("""
    <style>

    [data-testid="stHeader"]{
                background-color:rgba(255,255,255,0);
                }

    [data-testid="stAppViewContainer"] {
                    background-image:  linear-gradient(155deg, rgba(12, 13, 20, 0.200) 0%, rgba(2, 3, 3, 0.500) 100%),url("https://wallpapercave.com/wp/wp12814430.jpg");
                    background-size: cover;
                    background-repeat: no-repeat;
                    background-attachment: fixed;
                    height: 100%;}

    #map_div{
                    margin-bottom:100px;

                }
                </style>                


    """, unsafe_allow_html=True)
##########################################################


st.markdown("""
    <style>

    [data-testid="stHeader"]{
     background-color:rgba(255,255,255,0);
     }

    #hotel-luxury{
    font-size:60px;
    margin-top:150px;
    margin-left:150px;
    font-family:serif;
    color:white;
    margin-bottom:400px;
    }

    [data-testid="stAppViewContainer"] {
        background-image:  linear-gradient(155deg, rgba(12, 13, 20, 0.200) 0%, rgba(2, 3, 3, 0.500) 100%),url("https://wallpapercave.com/wp/wp12814430.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        height: 100%;

    }
    </style>
    """

            , unsafe_allow_html=True)

########################################################

st.markdown("""
    <style>

    [data-testid="stHeader"]{
                background-color:rgba(255,255,255,0);
                }

    [data-testid="stAppViewContainer"] {
                    background-image:  linear-gradient(155deg, rgba(12, 13, 20, 0.200) 0%, rgba(2, 3, 3, 0.500) 100%),url("https://wallpapercave.com/wp/wp12814430.jpg");
                    background-size: cover;
                    background-repeat: no-repeat;
                    background-attachment: fixed;
                    height: 100%;}

    #map_div{
                    margin-bottom:100px;

                }
                </style>                


    """, unsafe_allow_html=True)