import streamlit as st
st.set_page_config(page_title="chambres")
def chambres():
    '''

    your code here

    '''




    #static for all pages

    st.markdown("---")
    st.subheader("Avis des clients")
    st.write("Voici ce que nos clients disent de nous:")

    testimonial_1, testimonial_2, testimonial_3 = st.columns(3)

    with testimonial_1:
        st.write('"Expérience incroyable!"')
        st.caption("- Alice")

    with testimonial_2:
        st.write('"Personnel très accueillant."')
        st.caption("- Karim")

    with testimonial_3:
        st.write('"Séjour luxueux et inoubliable."')
        st.caption("- Leila")
    # ---------------- FAQ Section ----------------
    st.title("Foire aux Questions (FAQ)")

    with st.expander("Quels sont les horaires d'ouverture de l'hôtel ?"):
        st.write("Notre hôtel est ouvert 24h/24 et 7j/7 pour vous accueillir.")

    with st.expander("Est-ce que l'hôtel propose un service de navette ?"):
        st.write("Oui, nous proposons un service de navette aéroport sur réservation.")

    with st.expander("Les animaux de compagnie sont-ils autorisés ?"):
        st.write("Oui, les animaux de compagnie sont acceptés sous certaines conditions.")

    with st.expander("Proposez-vous des formules tout compris ?"):
        st.write("Oui, nous avons plusieurs formules adaptées à vos besoins et préférences.")

    st.caption("NOM et PRENOMS: **********************")