import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(layout="wide")
nav1,nav2,nav3,nav4=st.tabs(["home","agence","reservations","chambre"])
st.title("Welcome to home page")
agences=st.Page(
    page="views/Agences.py",
    title="Agences")
Chambres=st.Page(
    page="views/Chambre.py",
    title="Chambers",
)
Reservations=st.Page(
    page="views/Reservations.py",
    title="Reservations",
)
with nav2:
    st.navigation(pages=[agences]).run()
with nav3:
    st.navigation(pages=[Chambres]).run()
with nav4:
    st.navigation(pages=[Reservations]).run()


def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        body,html{{
            height:100%;
        }}
        .stAppToolbar.st-emotion-cache-14vh5up.e3g0k5y2{{
        display: none;
        
        
        }}
        stAppHeader.st-emotion-cache-gquqoo.e3g0k5y1{{
        visibility:hidden;
        display:none;
        
        }}

         [data-testid="stAppViewContainer"]{{
            background-image:  linear-gradient(155deg, rgba(10, 12, 6, 0.432) 0%, rgba(120, 145, 110, 0.336) 100%),url(https://imgs.search.brave.com/y96KuFdeeWxhSqzrOfwYzF46HpxgmNKwD0Qd_Pc_Syw/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly93YWxs/cGFwZXJiYXQuY29t/L2ltZy8xNDU1MjY2/MzctbHV4dXJ5LWhv/dGVsLXdhbGxwYXBl/ci5qcGc);
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
    height: 95vh;
    margin-bottom: 100px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_url()
