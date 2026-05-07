import streamlit as st

st.title("Website St")

name = st.text_input("Enter your name")
email = st.text_input("Enter your email")
phone = st.text_input("Enter your phone number")
Address = st.text_input("Fill your Address")
if st.button("Submit"):
    st.success(f"Hello {name}, Your data submitted successfully!")