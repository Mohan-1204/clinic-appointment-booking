import os
import smtplib
import streamlit as st
from email.mime.text import MIMEText

def send_email(receiver_email, name, age, selected_doctor, doctor_time, treatment):

    sender_email = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")

    st.write("Sender:", sender_email)
    st.write("Receiver:", receiver_email)

    body = f"""
Hello {name},

Your appointment is confirmed.

Doctor: {selected_doctor}
Time: {doctor_time}
Treatment: {treatment}
"""

    msg = MIMEText(body)
    msg['Subject'] = "Appointment Confirmation"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587, timeout=20)

        server.starttls()

        server.login(sender_email, password)

        server.sendmail(
            sender_email,
            receiver_email,
            msg.as_string()
        )

        server.quit()

        st.success("MAIL SENT")
        return True

    except Exception as e:
        st.error(str(e))
        return False