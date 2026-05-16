import streamlit as st


st.set_page_config(
    page_title="Scratch Website",
    layout="wide"
)

st.title("Shopping Website")


name = st.text_input("Enter your name")
email = st.text_input("Enter your email")
phone = st.text_input("Enter your phone number")
Address = st.text_input("Fill your Address")
if st.button("Submit"):
    st.success(f"Hello {name}, Your data submitted successfully!")

st.header("Images")
col1, col2 = st.columns(2)

with col1:

    # st.markdown('<div class="feature-box">', unsafe_allow_html=True)
    st.image("https://images.pexels.com/photos/14553705/pexels-photo-14553705.jpeg")

    st.write(
        "Build websites and apps quickly using AI-powered tools."
    )

    st.markdown('</div>', unsafe_allow_html=True)

with col2:

    # st.markdown('<div class="feature-box">', unsafe_allow_html=True)
    st.image("asset/IMG_1026.jpg")

    st.write(
        "Build websites and apps quickly using AI-powered tools."
    )

    st.markdown('</div>', unsafe_allow_html=True)