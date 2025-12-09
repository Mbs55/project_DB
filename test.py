import streamlit as st
import os
import pandas as pd
st.title("Welcome To Sign-up Page:")
form_values={
    "Username":"",
    "Email":"",
    "Age":"",
    "Password":"",
    "Confirmation_Password":""
}
with st.form(key="User_infos"):
    form_values["Username"]=st.text_input("Enter your Username: ")
    form_values["Email"]=st.text_input("Enter your Email Address: ")
    form_values["Age"]=st.number_input("Enter your Age: ",min_value=18,max_value=100)
    form_values["Password"]=st.text_input("Enter a Password: ")
    form_values["Confirmation_Password"]=st.text_input("Confirm your Password: ")
    submit=st.form_submit_button("Submit Form")
    if (submit):
        if (all(form_values.values())):
            if (form_values["Password"] == form_values["Confirmation_Password"]):
                st.write("User created successfully")
            else:
                st.warning("Passwords does not match ")
        else:
            st.warning("Please fill in all the information")



st.caption("for more information contact us")









