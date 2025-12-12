import streamlit as st
st.set_page_config(page_title="AGENCES")
st.write("Bienvenue a la page d agence ici vous auriez toutes les infos a propos des agences pres de vous\n")
conn=st.connection(name="hotel")
query=conn.query("select * from AGENCE_DE_VOYAGE;")
st.write("Table des agences:")
st.write(query)
