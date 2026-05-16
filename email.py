import streamlit as st

import smtplib

from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart

st.set_page_config(
    page_title="Contact Form",
    layout="centered"
)

st.title("Send Message")

# USER INPUTS

user_name = st.text_input(
    "Your Name"
)

user_email = st.text_input(
    "Your Email"
)

subject = st.text_input(
    "Subject"
)

message_text = st.text_area(
    "Message"
)

# FIXED RECEIVER EMAIL
receiver_email = "ariyajuddin72@gmail.com"

# SENDER EMAIL
sender_email = "ariyajuddin721@gmail.com"

# GMAIL APP PASSWORD
sender_password = "wxuz vsze vvea lrdo"

# SEND BUTTON

if st.button(
    "Send Message",
    use_container_width=True
):

    try:

        # CREATE EMAIL
        message = MIMEMultipart()

        message["From"] = sender_email

        message["To"] = receiver_email

        message["Subject"] = subject

        body = f"""
        Name: {user_name}

        User Email: {user_email}

        Message:
        {message_text}
        """

        message.attach(
            MIMEText(body, "plain")
        )

        # SMTP SERVER
        server = smtplib.SMTP(
            "smtp.gmail.com",
            587
        )

        server.starttls()

        # LOGIN
        server.login(
            sender_email,
            sender_password
        )

        # SEND EMAIL
        server.sendmail(
            sender_email,
            receiver_email,
            message.as_string()
        )

        server.quit()

        st.success(
            "Message Sent Successfully"
        )

    except Exception as e:

        st.error(
            f"Error: {e}"
        )