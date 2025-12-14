import streamlit as st
st.set_page_config(page_title="reservation",layout="wide")

def reservation():
    '''

       your code here

    '''

    # static for all pages

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

reservation()